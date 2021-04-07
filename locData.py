from fileio import file_to_dict
import numpy

locDataFile = 'data/malls.txt'
sgMinLng = 631 #lng 103.631 #min longtitude, 3dp
sgMaxLng = 999              #max longtitude, 3dp
lngRange = sgMaxLng - sgMinLng

sgMinLat = 238 #lat 1.238 #min latitude, 3dp
sgMaxLat = 466            #max latitude, 3dp
latRange = sgMaxLat - sgMinLat


def getLocFromFile():
    locDict = file_to_dict(locDataFile) #putting in location into a dict
    #for each coord, we want to trucante it to the first 3dp
    for k, v in locDict.items(): #cr
        x,y = v 
        x = x.split('.')[1][:3] #trucante the value of x to the first 3dp
        y = y.split('.')[1][:3] #trucante the value of x to the first 3dp
        x = int(x)-sgMinLat  #set the value of x, to be the int value of(x) minus the minimum latitude
        y = int(y)-sgMinLng  #set the value of y, to be the int value of(y) minus the minimum longtitude
        locDict[k] = (x,y) #setting a coordinate value, for each index in locDict
    return locDict 
