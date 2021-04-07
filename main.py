## @file main.py
#
# @brief this file contains all the neccessary information to determine whether a person has covid
#
# @author Jodie
#

#Imports
#local imports
import locData
import peopleData
import comparison
import randomFn
import UIdata
#library imports
import multidict


chanceToCatchCovid = 3  #percentage chance of catching covid(3% chance)
locDict = locData.getLocFromFile() #retrieve location data by calling function getLocFromFile() 
peopleData.generatePeople(100) #generate the amount of person data needed  
peopleData.generateLoctime(locDict) #generate timestamp for each person generated

def setLocWarning(person):
    """! This method set a location warning for a person
       brief: if a person has a location warning, a number "3" will be tag to them
    """
    person.setTag(peopleData.personTag.locationWarning)  

def setCloseWarning(person): 
    """! This method set a close contact warning for a person
       brief: if a person has a close contact warning, a number "2" will be tag to them
    """
    person.setTag(peopleData.personTag.closeWarning) 

def setSpread(person): #function to set covid spread rate
    #real life use case, u ask them to go swab
    #therefore there actually isnt that much recursion
    """! This method set covid spread rate 
    """
    if randomFn.randChance(chanceToCatchCovid): 
        hasCovid(person.token)

def hasCovid(token): #function to check if the person has covid
    """! This method set a location warning for a person
       brief: if a person has covid, a number "1" will be tag to them
    """
    person = peopleData.listOfPpl[token] #establishing person as an object to be easily reference
    person.setTag(peopleData.personTag.covid) #if a person has a location warning, a number "1" will be tag to them
    #run through all locations that person has been
    loc = person.getLoc() #retriving all location that person has been too
    prev = None #to check for location duplicates for count
                #since people can go to the same location many times
    for location, value in loc.items(): #look through all the locations
        if prev != location:  #check if the mall a covid infected person has been to is not on the list
            peopleData.covidLoc[location] += 1  #add the location into the list
        if len(peopleData.listOfPplPerLoc[location]) <= 1: #check the amount of people in the covid infected location
            continue
        else:
            #more than one person has been to location
            #check everyone that has been to location
            for tokenX in peopleData.listOfPplPerLoc[location]: #check the token for each person in th covid infected location
                personX = peopleData.listOfPpl[tokenX] #establishing personX as an object for easy reference
                #for each person
                locX = personX.getLoc() #retrieving all the location that personX has been too
                #check timeframe
                #this may change bc need to check with covid visit window

                #need to loop through duplicate keys/values, for the same location as it is a multdict
                xLocKeyList = locX.getall(location)
                for x in xLocKeyList:
                    if comparison.checkTimeStamp(locX[location], value): #checking the time personX check in to all the locations he visited
                        print("coincide!") #if their timing meets, print out conincide
                        print(token, "and", personX.token, "were at", location)
                        setCloseWarning(personX) #set a close contact warning on personX
                        setSpread(personX) 
                        print("end")
                        #add edge
                        UIdata.addPeopleConnectJson({"from": person.name, "to": personX.name})
                    else:
                        if personX.persontags == peopleData.personTag.nothing.value: #check if the person has a nothing value
                            print("same location!") 
                            setLocWarning(personX)  #set a location warning on personX
        prev = location


#setting how many people to have covid 
#randomly setting 2 people catch the virus
hasCovid(4) 
hasCovid(6) 
UIdata.createJson()