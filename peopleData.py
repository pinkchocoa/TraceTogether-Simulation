from enum import Enum #https://www.tutorialspoint.com/enum-support-for-enumerations-in-python
import multidict #pip install multidict https://pypi.org/project/multidict/ https://multidict.readthedocs.io/en/stable/
import randomFn
import datetime

listOfPpl = list()

class personTag(Enum):
    nothing = 0
    covid = 1
    closeWarning = 2

class person:
    def __init__(self,token,name,phoneNumber):
            super().__init__()
            self.token=token #identification
            self.name=name #IC number as the name
            self.phoneNumber=phoneNumber #Phone number with 8 digits
            #self.email=email
            self.persontags=personTag.nothing.value
            
            #data structs
            self.btsignal = set()
            self.location = multidict.MultiDict() #allows multiple keys
            self.btcount=0 #-The number of bluetooth signal made

    def print(self):
        print("token:", self.token)
        print("name:", self.name)
        print("phone number:", self.phoneNumber)
        print("tag:", personTag(self.persontags).name)
        for x,y in self.location.items():
            print(x, y)

def generateLocCheckIn(locData):
    locIdx = list(locData.keys())
    print(locIdx)
    return locIdx
        
def generatePeople(x):
    for id in range(x):
      listOfPpl.append(person(id, randomFn.randName(),randomFn.randInt(80000000,99999998)))

def generateLoctime(locData):
    locIdx = generateLocCheckIn(locData)
    for person in listOfPpl:
        totalLoc = randomFn.randInt(1,5)
        time = randomFn.random_timestamp(totalLoc, 1)
        for x in range(totalLoc):
            place = randomFn.randInt(0, len(locIdx)-1)
            person.location.add(locIdx[place], time[x])
        
            

# locDict = locData.getLocFromFile()
# generatePeople(5)
# generateLoctime(locDict)
# for x in listOfPpl:
#     x.print()