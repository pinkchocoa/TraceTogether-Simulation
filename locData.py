from fileio import file_to_dict
import numpy
from aStar import astar

locDataFile = 'malls.txt'
sgMinLng = 631 #lng 103.631
sgMaxLng = 999
lngRange = sgMaxLng - sgMinLng

sgMinLat = 238 #lat 1.238
sgMaxLat = 466
latRange = sgMaxLat - sgMinLat

def createMaze():
    #gotta convert coords to x,y that i can use for a maze
    #creating a xrange x yRange maze
    maze = numpy.zeros((latRange, lngRange), dtype=int)
    return maze

def getLocFromFile():
    locDict = file_to_dict(locDataFile)
    print(locDict)
    
    

start = (289-sgMinLat, 849-sgMinLng)
end = (291-sgMinLat, 820-sgMinLng)
path = astar(createMaze(), start, end)
print(path)