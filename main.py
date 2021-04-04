from aStar import astar
import locData
import peopleData
import multidict 
import comparison

maze = locData.createMaze()
locDict = locData.getLocFromFile()
peopleData.generatePeople(10)
peopleData.generateLoctime(locDict)
for x in peopleData.listOfPpl:
    x.print()

def hasCovid(token):
    person = peopleData.listOfPpl[token]
    person.setTag(peopleData.personTag.covid)
    #run through all locations that person has been
    loc = person.getLoc()
    for x in loc.keys():
        if len(peopleData.listOfPplPerLoc[x]) == 1:
            continue
        else: #more than one person has been to location
            #check everyone that has been to location
            for personX in peopleData.listOfPpl:
                #for each person
                locX = personX.getLoc()
                if x in locX: #person as been to said location too
                    #check timeframe
                    if comparison.checkTimeStamp(locX[x], loc[x]):
                        print("coincide!")
                        print(person.token, "and", personX.token, "were at", x)
                        print("end")
    
hasCovid(4)
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