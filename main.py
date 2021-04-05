from aStar import astar
import locData
import peopleData
import multidict 
import comparison
import randomFn
import UIdata

chanceToCatchCovid = 3
maze = locData.createMaze()
locDict = locData.getLocFromFile()
peopleData.generatePeople(100)
peopleData.generateLoctime(locDict)
for x in peopleData.listOfPpl:
    x.print()

def setLocWarning(person):
    person.setTag(peopleData.personTag.locationWarning)
    if randomFn.randChance(chanceToCatchCovid): 
        hasCovid(person.token)

def hasCovid(token):
    person = peopleData.listOfPpl[token]
    person.setTag(peopleData.personTag.covid)
    #run through all locations that person has been
    loc = person.getLoc()
    prev = None
    for x in loc.keys():
        if prev != x:
            peopleData.covidLoc[x] += 1 #remember to remove duplicates
        if len(peopleData.listOfPplPerLoc[x]) == 1:
            continue
        else: #more than one person has been to location
            #check everyone that has been to location
            for personX in peopleData.listOfPpl:
                #for each person
                locX = personX.getLoc()
                if x in locX: #person as been to said location too
                    #check timeframe
                    #this may change bc need to check with covid visit window
                    if comparison.checkTimeStamp(locX[x], loc[x]):
                        print("coincide!")
                        print(token, "and", personX.token, "were at", x)
                        setLocWarning(personX)
                        print("end")
                        #add edge
                        UIdata.addPeopleConnectJson({"from": person.name, "to": personX.name})
        prevLoc = x
    
hasCovid(4)
hasCovid(6)

print(peopleData.covidLoc)

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