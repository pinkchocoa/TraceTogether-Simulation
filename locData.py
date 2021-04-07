from fileio import file_to_dict
import numpy

locDataFile = 'data/malls.txt'
sgMinLng = 631 #lng 103.631
sgMaxLng = 999
lngRange = sgMaxLng - sgMinLng

sgMinLat = 238 #lat 1.238
sgMaxLat = 466
latRange = sgMaxLat - sgMinLat

#not in used
def createMaze():
    #gotta convert coords to x,y that i can use for a maze
    return numpy.zeros((latRange, lngRange), dtype=int)

def getLocFromFile():
    #changing the location coords to x,y for the maze
    locDict = file_to_dict(locDataFile)
    #print(locDict)
    #for each coord, we want to trucante it to the first 3dp
    for k, v in locDict.items():
        x,y = v
        x = x.split('.')[1][:3]
        y = y.split('.')[1][:3]
        x = int(x)-sgMinLat
        y = int(y)-sgMinLng
        locDict[k] = (x,y)
    #print(locDict)
    return locDict 

# path = astar(createMaze(), start, end)
# print(path)
# getLocFromFile()