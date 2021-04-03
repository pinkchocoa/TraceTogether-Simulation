from datetime import datetime #this is to retrieve date and time
import random
# base for trace together

# data, list of dict?
# whats in the data

# what output do we want 

#import date

#create two enums, one for cluster rank, one for bt signal

#with the token, we can search this class to get their number to inform them
#if we usetelegram as UI, we can change the contact to telegram usernam
#PersonData Class
class personData:

    def __init__(self,name,phoneNumber,email,persontags,token,timestamp,locationtag,btsignal2,btcount):
        self.name=name #IC number as the name
        self.phoneNumber=phoneNumber #Phone number with 8 digits
        self.email=email
        self.persontags=persontags #-0 = covid patient, 1 = close contact, 2= Nothing
        self.token=token #-This is their primary key
        self.timeStamp.append(timeStamp) #-timestamp[checkin,checkout] timestamp[0] && timestamp[1] means the date and time range for 1 location in locationtag[i]
        self.locationtag.append(locationtag) #-locationtag[heartland]
        self.btsignals.append(btsignal2) #-btsignalArray2=[1,1,0,1,0,0,1] in the btsignalArray2=[i], i means amount of people, 1 means close contact condition is true! 0 means close contact condition is false
        self.btcount=btcount #-The number of bluetooth signal made

    def addLocation(self,location):
        self.locationtag.append(location)

    def addTimeStamp(self,time):
        self.timestamp.append(time)

    def termtag(persontags): #labeling for the persontag
        label = ""
        if persontags == 0:
            label = "Covid Patient"
        if persontags == 1:
            label = "Close Contact"
        if persontags == 2:
            label = "Nothing"
        
        
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


def btSignal(btsignalArray): #-(time, token1, token2)
    t = 600 #-This must be set accordingly to seconds, 600seconds means 10 mins, this number can be random!
    #how to start timer? aka where to use this function
    for i in range(len(btSignalArray)):
        if btsignalArray[i] == 1:
            if timer(t):
                btsignalArray2.append(1)
            else: 
                btsignalArray2.append(0)
                
        #if more than 10 mins
        #means they fulfil the covid visit window?

def timer(t): #-this timer is countdown timer, if we need to use
    while t:
        min,secs = divmod(t,60)
        timer ='{:02d}:{:02d}'.format(mins,secs)
        time.sleep(1)
    return True

def btcount(count):
    count = 0
    for i in range(len(btsignalArray2)):
        if i == 1:
            count+=1

class btConnection: 
    firstToken=-1
    secondToken=-1
    time1=0
    time2=0

    def __init__(self,firstToken,secondToken):
        self.firstToken=firstToken
        self.secondToken=secondToken

    def startTimer(self, time):
        self.time1=time

    def stopTimer(self, time):
        self.time2=time

    def checkDuration(self):
        return self.time2-self.time1

    
    #how to decide bt signal == contact (also need to keep time in acc?)
    #bc this connection does not use physical location?
    
 
class location:
    location=[]
    timestamp=[] #-finaly timestamp return to each person
    timestamp1=0 #-day_month_year_time (check in time)
    timestamp2=0 #-day_month_year_time (check out time)

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
        if self.selection is 0: #This is covid patient
            self.covid=True
            self.warning=True
        elif self.selection is 1: #This is close contact person
            self.covid=False
            self.warning=True
        elif self.selection is 2: #This dude got nothing
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
    
class locationTags: #Work in Progress
    locationName=""
    covidCounter=-1
    clusterRank=-1
    def covidCounterIncrement(self):
        covidCounter+=1

    
    #function to set clusterrank before we display the data
    
#algo to be used
#jodie interpretation
#-aloy and jiashu comments
#refer to that long ass picture/infographic in discord

#algo: to even set the tag for the person to begin with we need to sift through data to find the person?? but technically if we use database or map key then we dont?
#1. need a field to say that this person has covid -Persontag(done)
#1.1 get all locations that person has been (location class) -locationtag(Work in progress)
#1.15 for each location, we keep a counter of how many people have covid there? -(location tag and btcounter)
#search algo here (1.2)
#1.2 check other people's timestamp and location that matches - timestamp[i] && timestamp[i+1] refers to check in and out pointing to locationtag[0] refers to one location.
#potential algo, how we speed up calculations or skip if we dont need to calculate at all? (1.3)
#1.3 check bluetooth to see if they are in covid visit window (btconnection class) -Use timestamp[]
#2. from that, get all record that is in the covid visit window with that guy -use btsignal2[]
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
personalInfo = [[0 for i in range(9)] for j in range(7)]#2d array for 7 ppl with 5 element each
btSignalArray=[1,1,1,1,0,0,1]#1 stands for distance less than 10metre. Should be randomly generated array. Determine the distance
btsignalArray2=[1,1,0,1,0,0,1]#1 stamds for time more then 10 mins. Should be randomly generated array. Determine the time

#-static dataset for 7 person and 2 locations
lo1 = locationTags()
lo2 = locationTags()
lo1.locationName='Heartland'
lo2.locationName='Tenmile'

p1=personData('A', 91234567, 'a@gmail.com', 0, 1, 100320201700, 'heartland', 1, 0)
p1.addTimeStamp(1003202100)

p2=personData('B', 91234566, 'b@gmail.com', 1, 2, 100320201630, 'heartland', 1, 0)
p2.addTimeStamp(1003201800)

p3=personData('C', 91234565, 'c@gmail.com', 2, 3, 100320201200, 'heartland', 1, 0)
p3.addTimeStamp(1003201730)

p4=personData('D', 91234564, 'd@gmail.com', 1, 4, 100320201710, 'heartland', 1, 0)
p4.addTimeStamp(1003201830)
p4.addTimeStamp(1003201900)
p4.addTimeStamp(1003202000)
p4.addLocation('tenmile')

p5=personData('E', 91234563, 'e@gmail.com', 2, 5, 090320201000, 'heartland', 0, 0)
p5.addTimeStamp(0903201200)

p6=personData('F', 91234562, 'f@gmail.com', 2, 6, 100320201230, 'tenmile', 0, 0)
p6.addTimeStamp(1003201600)

p7=personData('G', 91234561, 'g@gmail.com', 1, 7, 100320201730, 'tenmile', 1, 0)#fourth element will be random generated
p7.addTimeStamp(1003201940)

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
    personalInfo[i][5]=personDict[count].timestamp
    personalInfo[i][6]=personDict[count].locationtag
    personalInfo[i][7]=personDict[count].btsignal2
    personalInfo[i][8]=personDict[count].btcount
    count+=1
    

#sample of data
#as well as what the output will be

#- output for tracing will be:
#- 0->1->3->6, 0 is the covid patient

# -btcount means how many people this person had close contact with
#- P1 btcount = 1, label = Covid Patient
#- P2 btcount = 1, label = Close Contact
#- P3 btcount = 0, label = Nothing
#- P4 btcount = 2, label = Close Contact
#- P5 btcount = 0  label = Nothing
#- P6 btcount = 0  label = Nothing
#- P7 btcount = 1  label = Close Contact
print(algothatwewilluse(data))