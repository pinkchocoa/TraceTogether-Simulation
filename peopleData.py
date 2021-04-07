## @file main.py
#
# @brief this file contains all the neccessary information to determine whether a person has covid
#
# @author Jodie
#


#Imports
from enum import Enum #https://www.tutorialspoint.com/enum-support-for-enumerations-in-python
import multidict #pip install multidict https://pypi.org/project/multidict/ https://multidict.readthedocs.io/en/stable/
import randomFn
import datetime
from fileio import file_to_dict

listOfPpl = list() #stores list of person objects
listOfPplPerLoc = {} #stores location as key and set() of people as value
covidLoc = {} #stores location as key and int of people that has covid as value


class personTag(Enum):
    """! This class sets an integer variable tag to a person 
    """
    nothing = 0  
    covid = 1 
    closeWarning = 2 
    locationWarning = 3

class person:
    def __init__(self,token,name,phoneNumber): 
            super().__init__()
            self.token=token #idx, like ic or tracetgt token
            self.name=name #name of person
            self.phoneNumber=phoneNumber #Phone number with 8 digits
            self.persontags=personTag.nothing.value #status
            
            #data structs
            self.location = multidict.MultiDict() #allows multiple keys

    def print(self):
        print("token:", self.token)
        print("name:", self.name)
        print("phone number:", self.phoneNumber)
        print("tag:", personTag(self.persontags).name)
        for x,y in self.location.items():
            print(x, y[0], y[1])
    
    def setTag(self, tag): 
        self.persontags = tag.value

    def getLoc(self):
        return self.location

def getLocFromFile():
    locDataFile = 'data/malls.txt'
    locDict = file_to_dict(locDataFile) #putting in location into a dict
    return list(locDict.keys()) #only want the index actually

def generateLocCheckIn(locData): #function to initiliaze variables for location data
    for x in locData:
        listOfPplPerLoc[x] = set()
        covidLoc[x] = 0

def generateLocTime(locIdx): #function to generate check in time
    generateLocCheckIn(locIdx)
    for person in listOfPpl: 
        totalLoc = randomFn.randInt(1,14) 
        time = randomFn.random_timestamp(totalLoc, 1)
        for x in range(totalLoc):
            place = randomFn.randInt(0, len(locIdx)-1) #for each location
            person.location.add(locIdx[place], time[x]) #add a time
            listOfPplPerLoc[locIdx[place]].add(person.token)

def generatePeople(x): #function to generate people data
    locIdx = getLocFromFile()
    for id in range(x):
      listOfPpl.append(person(id, randomFn.randName(),randomFn.randInt(80000000,99999998)))

    generateLocTime(locIdx)

