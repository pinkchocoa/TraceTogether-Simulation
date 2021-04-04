from aStar import astar
import locData
import peopleData

maze = locData.createMaze()
locDict = locData.getLocFromFile()
peopleData.generatePeople(5)
peopleData.generateLoctime(locDict)
for x in peopleData.listOfPpl:
    x.print()

def hasCovid(token):
    peopleData.listOfPpl[token].setTag(peopleData.personTag.covid)

hasCovid(4)

for x in peopleData.listOfPpl:
    x.print()
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