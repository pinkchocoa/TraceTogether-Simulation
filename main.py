## @file main.py
#
# @brief this file contains the main function of our project
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

def setSpread(person):
    """! function to set covid spread rate
    this is a recursion function to tag people with covid
    while it is recursion, 
    it will never hit recursion depth in real life use cases
    however as the entire data set is randomised, it is possible to
    @param person person to check covid spread rate to
    """
    if randomFn.randChance(chanceToCatchCovid): 
        print("covid spread", person)
        hasCovid(person)

def hasCovid(token):
    """!hasCovid function sets a person status with covid
    @param token token is the identifier for a person 
    """
    personWCovid = peopleData.listOfPpl[token] 
    personWCovid.setTag(peopleData.personTag.covid) #set person to covid
    loc = personWCovid.getLoc() #location data
    for location, value in loc.items():
        peopleData.covidLoc[location].add(token)
        if len(peopleData.listOfPplPerLoc[location]) <= 1: #only 1 unique person that has been to the location
            continue #we dont need to check
        else:
            #check everyone that has been to location
            for tokenX in peopleData.listOfPplPerLoc[location]: #get each unique person that has been to said location
                closePerson = peopleData.listOfPpl[tokenX]
                if closePerson.persontags == peopleData.personTag.covid.value:
                    continue
                cpLocData = closePerson.getLoc() #grab the location data for closePerson
                #need to loop through duplicate keys/values, for the same location as it is a multdict
                locationCheckIns = cpLocData.getall(location) #grab a list of timestamp for the same location
                for checkIn in locationCheckIns:
                    if comparison.checkTimeStamp(checkIn, value):
                        #print(token, "and", closePerson.token, "were at", location)
                        #set a close contact warning on closePerson
                        closePerson.setTag(peopleData.personTag.closeWarning) 
                        setSpread(closePerson.token) #chance of spreading the virus
                        #add edge for network graph/connection display
                        UIdata.addPeopleConnectJson({"from": personWCovid.name, "to": closePerson.name})
                    else: #they have both been to the same place but not at the same time
                        if closePerson.persontags == peopleData.personTag.nothing.value:
                            #print("same location!") 
                            #set a location warning on closePerson
                            closePerson.setTag(peopleData.personTag.locationWarning)


#setting people to have covid 
#randomly setting 2 people catch the virus
hasCovid(4) 
hasCovid(6) 
UIdata.createJson()