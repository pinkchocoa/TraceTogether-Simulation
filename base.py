# base for trace together

# data, list of dict?
# whats in the data

# what output do we want 

#import date

#create two enums, one for cluster rank, one for bt signal

#with the token, we can search this class to get their number to inform them
#if we use telegram as UI, we can change the contact to telegram username
class personData:
    name:""
    phoneNumber=999
    email=""
    token=-1

class traceData:
    token=-1 #int primary key
    timestamp="" #date, and in what format
    
    #payload of msg field? what this mean
    v=-1
    msg=""
    
    #MOH, we dont need this
    org=""
    
    #something about bt?
    modelP=""
    modelC=""
    
    #bluetooth signal
    rssi=-1
    txPower=-1
    
    
    phoneModel=""
    btSignal=1 #int, 1 will be weakest? or 1 be strongest?
    otherPhoneModels=""
    
    
    #insert data function
    
    #get data function
    
    #search data function
    
    #convert to DB function
    
    #convert from DB function

def btSignal(time, token1, token2):
    #how to start timer? aka where to use this function
    if time > 10: #if more than 10 mins
        #means they fulfil the covid visit window?

class btConnections:
    firstToken=-1
    secondToken=-1
    time=""
    
    #how to decide bt signal == contact (also need to keep time in acc?)
    #bc this connection does not use physical location?
    

class location:
    token=-1
    location=[]
    timestamp="" #data/time
    
    #insert whenever user scans a QR code
    #get function to return list of location
    #search function to check if user is at certain location

class personTags:
    token=-1
    covid=False #true for covid, false for no covid
    warning=False
    
    #insert(for each record in DB, create tags?)-
    #get/set functions
    #convert to DB function
    
    #convert from DB function
    
class locationTags:
    locationName=""
    covidCounter=-1
    clusterRank=-1
    
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

#sample of data
#as well as what the output will be

print(algothatwewilluse(data))