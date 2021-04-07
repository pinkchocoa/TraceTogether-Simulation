#from aStar import astar
import locData
import peopleData
import multidict 
import comparison
import randomFn
import UIdata

chanceToCatchCovid = 3

locDict = locData.getLocFromFile()
peopleData.generatePeople(500)
peopleData.generateLoctime(locDict)

def setLocWarning(person):
    person.setTag(peopleData.personTag.locationWarning)

def setCloseWarning(person):
    person.setTag(peopleData.personTag.closeWarning)

def setSpread(person):
    #real life use case, u ask them to go swab
    #therefore there actually isnt that much recursion
    if randomFn.randChance(chanceToCatchCovid): 
        hasCovid(person.token)

def hasCovid(token):
    person = peopleData.listOfPpl[token]
    person.setTag(peopleData.personTag.covid)
    #run through all locations that person has been
    loc = person.getLoc()
    prev = None #to check for location duplicates for count
    #since people can go to the same location many times
    for location in loc.keys():
        if prev != location:
            peopleData.covidLoc[location] += 1 
        if len(peopleData.listOfPplPerLoc[location]) <= 1:
            continue
        else: #more than one person has been to location
            #check everyone that has been to location
            for tokenX in peopleData.listOfPplPerLoc[location]:
                personX = peopleData.listOfPpl[tokenX]
                #for each person
                locX = personX.getLoc()
                #check timeframe
                #this may change bc need to check with covid visit window

                #need to loop through duplicate keys, not done yet
                if comparison.checkTimeStamp(locX[location], loc[location]):
                    print("coincide!")
                    print(token, "and", personX.token, "were at", location)
                    setCloseWarning(personX)
                    setSpread(personX)
                    print("end")
                    #add edge
                    UIdata.addPeopleConnectJson({"from": person.name, "to": personX.name})
                else:
                    if personX.persontags == peopleData.personTag.nothing.value:
                        print("same location!")
                        setLocWarning(personX)
        prev = location

hasCovid(4)
hasCovid(6)

#print(peopleData.covidLoc)

UIdata.createJson()
#peopleData.printLocSet()

#for x in peopleData.listOfPpl:
#    x.print()

#to do, set person to covid and location
#warnings should have time frame!

# start = 'Bugis Junction'
# end = 'Tampines Mall'
# path = astar(maze, locDict[start], locDict[end])
# print(path)
# print(len(path)) #90
# start = 'Bugis Junction'
# end = 'Marina Bay Sands'
# path = astar(maze, locDict[start], locDict[end])
# print(path)
# print(len(path)) #16

#jodie's todo
#create tags for locations as well
#use a star algo to set location tags
#think of a way to add weight for bluetooth and use graph algos
#make sure everything works and clean up codes