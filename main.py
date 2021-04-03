from aStar import astar
import locData
import peopleData

maze = locData.createMaze()
locDict = locData.getLocFromFile()
peopleData.generatePeople(5)
peopleData.generateLoctime(locDict)
for x in peopleData.listOfPpl:
    x.print()

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