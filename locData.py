from fileio import file_to_dict

def getLocFromFile():
    locDataFile = 'data/malls.txt'
    locDict = file_to_dict(locDataFile) #putting in location into a dict
    return list(locDict.keys()) 
