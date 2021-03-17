from datetime import datetime
import random
# base for trace together

# data, list of dict?
# whats in the data

# what output do we want 

#import date

#create two enums, one for cluster rank, one for bt signal

#with the token, we can search this class to get their number to inform them
#if we use telegram as UI, we can change the contact to telegram username

#PersonData Class
class personData:
    name=''
    phoneNumber=999
    email=""
    token=-1
    persontags=-1

    def __init__(self,name,phoneNumber,email,persontags,token):
        self.name=name
        self.phoneNumber=phoneNumber
        self.email=email
        self.persontags=persontags
        self.token=token


class traceData:
    token=-1 #int primary key
    timestamp="" #date, and in what format
    
    #payload of msg field? what this mean
    v=-1
    msg=""
    
    #bluetooth signal
    rssi=-1
    
    btSignal=1 #int, 1 will be weakest? or 1 be strongest?

    
    #insert data function
    
    #get data function
    
    #search data function
    
    #convert to DB function
    
    #convert from DB function

    btsignal=[]

def btSignal(btsignalArray): #(time, token1, token2)
    #how to start timer? aka where to use this function
    for i in range(len(btSignalArray)):
        if btsignalArray[i] == 1:

        #if more than 10 mins
        #means they fulfil the covid visit window?

class btConnections:
    firstToken=-1
    secondToken=-1
    time1=0
    time2=0

    def __init__(self,firstToken,secondToken):
        self.firstToken=firstToken
        self.secondToken=secondToken

    def startTimer(self):
        self.time1=

    def stopTimer(self):
        self.time2=

    def checkDuration(self):
        return self.time2-self.time1

    
    #how to decide bt signal == contact (also need to keep time in acc?)
    #bc this connection does not use physical location?
    
 
class location:
    token=-1
    location=[]
    timestamp1=0 #data/time
    timestamp2=0

    def __init__(self,token):
        self.token=token

    def checkin(self):
        self.timestamp1=datetime.fromtimestamp(timestamp1)

    def checkOut(self):
        self.timestamp2=datetime.fromtimestamp(timestamp1)

    def getDuration(self):
        return self.timestamp2-self.timestamp1

    def getCheckIn(self):
        return self.timestamp1

    def getCheckOut(self):
        return self.timestamp2
   
    #insert whenever user scans a QR code
    #get function to return list of location
    #search function to check if user is at certain location

class personTags:
    token=-1
    covid=False #true for covid, false for no covid
    warning=False
    selection=-1

    def __init__(self,token,selection):
        self.token=token
        self.selection=selection

    def isCovid(self):
        if self.selection is 0:
            self.covid=True
            self.warning=True
        elif self.selection is 1:
            self.covid=False
            self.warning=True
        elif self.selection is 2:
            self.covid=False
            self.warning=False

    def setCovid(self,covid):
        self.covid=covid
    
    def getCovid(self):
        return self.covid

    def setWarning(self,warning):
        self.warning=warning
    
    def getWarning(self):
        return self.warning

    #insert(for each record in DB, create tags?)-
    #get/set functions
    #convert to DB function
    
    #convert from DB function
    
class locationTags:
    locationName=""
    covidCounter=-1
    clusterRank=-1
    def covidCounterIncrement(self):
        covidCounter+=1

    
    #function to set clusterrank before we display the data
    
#algo to be used
#my interpretation
#refer to that long ass picture/infographic in discord

#algo: to even set the tag for the person to begin with we need to sift through data to find the person?? but technically if we use database or map key then we dont?
#1. need a field to say that this person has covid
#1.1 get all locations that person has been (location class)
#1.15 for each location, we keep a counter of how many people have covid there?
#search algo here (1.2)
#1.2 check other people's timestamp and location that matches
#potential algo, how we speed up calculations or skip if we dont need to calculate at all? (1.3)
#1.3 check bluetooth to see if they are in covid visit window (btconnection class)
#2. from that, get all record that is in the covid visit window with that guy
#3. if theres is an overlap, we want to tag them with a warning


#function
def algothatwewilluse(data):
    #do things here
    pass
    #return something? if we dont return any data,
    #need to return True for success
    #and false for fail
    #lets pretend this gives us the output we want

def init():
#e.g. for what goes here: converting database into variables so we can use them
    pass
#technically traceTgt is a real time things
#where they constantly run through the data
#and add in stuff
#but for us, shall we assume that we are working with static data?
#so we basically just run update once?
def update(): 
#e.g. for what goes here: algo runs here
    pass

def end():
#e.g. for what goes here: save data in database?
    pass

#so basically our main will be
init()
update()
end()


#start of main
data = [] #example, we put in list first
personalInfo = [[0 for i in range(5)] for j in range(7)]#2d array for 7 ppl with 5 element each
btSignalArray=[1,1,1,1,0,0,1]#1 stands for distance less than 10metre. Should be randomly generated array. Determine the distance
btsignalArray2=[1,1,0,1,0,0,1]#
timeStamp=[[0 for i in range(2)] for j in range(7)]#2d array for each person checkin and checkout time 

lo1 = locationTags()
lo2 = locationTags()
lo1.locationName='Heartland'
lo2.locationName='Tenmile'

p1=personData('A', 91234567, 'a@gmail.com', 0, 1)
p2=personData('B', 91234566, 'b@gmail.com', 1, 2)
p3=personData('C', 91234565, 'c@gmail.com', 2, 3)
p4=personData('D', 91234564, 'd@gmail.com', 1, 4)
p5=personData('E', 91234563, 'e@gmail.com', 2, 5)
p6=personData('F', 91234562, 'f@gmail.com', 2, 6)
p7=personData('G', 91234561, 'g@gmail.com', 1, 7)#fourth element will be random generated

personDict={
    0  : p1,
    1  : p2,
    2  : p3,
    3  : p4,
    4  : p5,
    5  : p6,
    6  : p7
} 

count=0
for i in range(7):
    personalInfo[i][0]=personDict[count].name
    personalInfo[i][1]=personDict[count].phoneNumber
    personalInfo[i][2]=personDict[count].email
    personalInfo[i][3]=personDict[count].persontags
    personalInfo[i][4]=personDict[count].token
    count+=1
    

#sample of data
#as well as what the output will be

print(algothatwewilluse(data))