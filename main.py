## @file main.py
#
# @brief this file contains all the neccessary information to determine whether a person has covid
#
# @author Jodie
#

#Imports
#local imports
import peopleData
import comparison
import randomFn
import UIdata
#library imports
import multidict


chanceToCatchCovid = 3  #percentage chance of catching covid(3% chance)
peopleData.generatePeople(100)

def setLocWarning(person):
    """! This method set a location warning for a person
    """
    person.setTag(peopleData.personTag.locationWarning)  

def setCloseWarning(person): 
    """! This method set a close contact warning for a person
    """
    person.setTag(peopleData.personTag.closeWarning) 

def setSpread(person): #function to set covid spread rate
    #real life use case, u ask them to go swab
    #therefore there actually isnt that much recursion
    """! 
    """
    if randomFn.randChance(chanceToCatchCovid): 
        hasCovid(person.token)

def hasCovid(token):
    """!
    """
    personWCovid = peopleData.listOfPpl[token]
    personWCovid.setTag(peopleData.personTag.covid) #set person to covid
    loc = personWCovid.getLoc() #location data
    prev = None #to check for location duplicates for count
                #since people can go to the same location many times
    for location, value in loc.items():
        if prev != location:  #person already added to count for that location
            peopleData.covidLoc[location] += 1  #otherwise add
        if len(peopleData.listOfPplPerLoc[location]) <= 1: #only 1 unique person that has been to the location
            continue #we dont need to check
        else:
            #check everyone that has been to location
            for tokenX in peopleData.listOfPplPerLoc[location]: #get each unique person that has been to said location
                closePerson = peopleData.listOfPpl[tokenX]
                cpLocData = closePerson.getLoc() #grab the location data for closePerson
                #need to loop through duplicate keys/values, for the same location as it is a multdict
                locationCheckIns = cpLocData.getall(location) #grab a list of timestamp for the same location
                for checkIn in locationCheckIns:
                    if comparison.checkTimeStamp(checkIn, value):
                        print(token, "and", closePerson.token, "were at", location)
                        setCloseWarning(closePerson) #set a close contact warning on closePerson
                        setSpread(closePerson) #chance of spreading the virus
                        #add edge for network graph/connection display
                        UIdata.addPeopleConnectJson({"from": personWCovid.name, "to": closePerson.name})
                    else: #they have both been to the same place but not at the same time
                        if closePerson.persontags == peopleData.personTag.nothing.value:
                            print("same location!") 
                            setLocWarning(closePerson)  #set a location warning on closePerson
        prev = location


#setting people to have covid 
#randomly setting 2 people catch the virus
hasCovid(4) 
hasCovid(6) 
UIdata.createJson()