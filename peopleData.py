from enum import Enum #https://www.tutorialspoint.com/enum-support-for-enumerations-in-python
import multidict #pip install multidict https://pypi.org/project/multidict/ https://multidict.readthedocs.io/en/stable/
import randomFn
import datetime

listOfPpl = list() #stores list of person objects
listOfPplPerLoc = {} #stores location as key and set() of people as value
covidLoc = {} #stores location as key and int of people that has covid as value


class personTag(Enum):
    nothing = 0 #set a person without covid or any warnings, with a tag number 0 
    covid = 1 #set a person with covid, with a tag number 1 

    #closewarning is close contact ( person has been in the same mall same time on the same day)
    closeWarning = 2 #set a person with close contact, with a tag number 2

    #locationwarning is just a warning (person has been in the same mall within the last 7 days)
    locationWarning = 3 #set a person with location warning,  with a tag number 3

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
        print("token:", self.token)  #print person token number 
        print("name:", self.name) #print person name  
        print("phone number:", self.phoneNumber) #print person phone number
        print("tag:", personTag(self.persontags).name)  #print person tag 
        for x,y in self.location.items():
            print(x, y[0], y[1])
    
    def setTag(self, tag):  #function to set a person with a tag value(nothing = 0, covid = 1, close contact = 2, location warning = 3)
        self.persontags=tag.value #setting the tag value on person 

    def getLoc(self): #function to retrieve locations person has been too
        return self.location #return all the locations 

def generateLocCheckIn(locData): #function to initiliaze variables for location data
    locIdx = list(locData.keys()) 
    for x in locData.keys():
        listOfPplPerLoc[x] = set()
        covidLoc[x] = 0
    #print(locIdx)
    return locIdx
        
def generatePeople(x): #function to generate people data
    for id in range(x):
      listOfPpl.append(person(id, randomFn.randName(),randomFn.randInt(80000000,99999998))) #appending all the generated data into a list

def generateLoctime(locData): #function to generate check in time
    locIdx = generateLocCheckIn(locData) 
    for person in listOfPpl: #iterate through every person in the list
        totalLoc = randomFn.randInt(1,14) #function to generate a certain amount of check ins, 
        time = randomFn.random_timestamp(totalLoc, 1) # for each check in, a random time check in will be given, the value 1 is for today
        for x in range(totalLoc):  #generate a time for every location 
            place = randomFn.randInt(0, len(locIdx)-1) #for each location
            person.location.add(locIdx[place], time[x]) # for each location person has visited, add a time person visited to it
            listOfPplPerLoc[locIdx[place]].add(person.token)# add all the locations person has visited into a list based on different locations
        
def printLocSet():
    for x in listOfPplPerLoc.values():
        print("location", x)
        for i in x:
            print(i)

# locDict = locData.getLocFromFile()
# generatePeople(5)
# generateLoctime(locDict)
# for x in listOfPpl:
#     x.print()