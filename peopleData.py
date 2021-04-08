## @file peopleData.py
#
# @brief this file contains the dataset for a person
#


#Imports
#local imports 
import randomFn
import datetime
from fileio import file_to_dict

#library imports
from enum import Enum #https://www.tutorialspoint.com/enum-support-for-enumerations-in-python
import multidict #pip install multidict https://pypi.org/project/multidict/ https://multidict.readthedocs.io/en/stable/

listOfPpl = list() #stores list of person objects
listOfPplPerLoc = {} #stores location as key and set() of people as value
covidLoc = {} #stores location as key and int of people that has covid as value


class personTag(Enum):
    """! personTag class is an Enum for status tags
    """
    nothing = 0  #healthy
    covid = 1  #contracted covid
    closeWarning = 2 #close contact with someone w covid
    locationWarning = 3 #went to a place that someone w covid went to

class person:
    """!person class provides details for a person
    @var token token is the identifier for a person
    @var name name is the name of a person 
    @var phoneNumber is the number of a person 
    """    
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
        #print(tag.name)
        self.persontags = tag.value

    def getLoc(self):
        return self.location

def getLocFromFile():
    """!getLocFromFile function is retriving location details
    """  
    locDataFile = 'data/malls.txt'
    locDict = file_to_dict(locDataFile) #putting in location into a dict
    return list(locDict.keys()) #only want the index actually

def generateLocCheckIn(locData):
    """!generateLocCheckIn function initilizes variables for listOfPplPerLoc and covidLoc
    @param locData locData
    """  
    for x in locData:
        listOfPplPerLoc[x] = set()
        covidLoc[x] = set()

def generateLocTime(locIdx): 
    """!generateLocCheckIn function generates random checkin/out for each person 
    @param locIdx locIdx
    """  
    generateLocCheckIn(locIdx)
    for person in listOfPpl: 
        totalLoc = randomFn.randInt(1,14) 
        time = randomFn.random_timestamp(totalLoc, 1)
        for x in range(totalLoc):
            place = randomFn.randInt(0, len(locIdx)-1) #for each location
            person.location.add(locIdx[place], time[x]) #add a time
            listOfPplPerLoc[locIdx[place]].add(person.token)

def generatePeople(x):
    """!generatePeople function generates people data  
    @param x number of people to generate
    """  
    locIdx = getLocFromFile()
    for id in range(x):
      listOfPpl.append(person(id, randomFn.randName(),randomFn.randInt(80000000,99999998)))

    generateLocTime(locIdx)

