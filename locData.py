from fileio import file_to_dict
import numpy

locDataFile = 'data/malls.txt' #retriving all the data from malls.txt 
sgMinLng = 631 #lng 103.631 #setting a minimum longtitude, rounded up to 3 decimal place
sgMaxLng = 999              #setting a maximum latitude, rounded up to 3 decimal place
lngRange = sgMaxLng - sgMinLng #calculating the range of values for longtitude 

sgMinLat = 238 #lat 1.238 #setting a minimum latitude, rounded up to 3 decimal place
sgMaxLat = 466            #setting a maximum latitude, rounded up to 3 decimal place
latRange = sgMaxLat - sgMinLat #calculating the range of values for latitude 

def createMaze():
    #not in use
    #gotta convert coords to x,y that i can use for a maze
    return numpy.zeros((latRange, lngRange), dtype=int)

def getLocFromFile():
    #changing the location coords to x,y for the maze
    locDict = file_to_dict(locDataFile) #putting in location into a dict
    #print(locDict)
    #for each coord, we want to trucante it to the first 3dp
    for k, v in locDict.items(): #cr
        x,y = v 
        x = x.split('.')[1][:3] #trucante the value of x to the first 3dp
        y = y.split('.')[1][:3] #trucante the value of x to the first 3dp
        x = int(x)-sgMinLat  #set the value of x, to be the int value of(x) minus the minimum latitude
        y = int(y)-sgMinLng  #set the value of y, to be the int value of(y) minus the minimum longtitude
        locDict[k] = (x,y) #setting a coordinate value, for each index in locDict
    #print(locDict)
    return locDict 

# path = astar(createMaze(), start, end)
# print(path)
# getLocFromFile()