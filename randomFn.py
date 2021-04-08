"""! This file contains all the function to generate random data. 
"""

import random #https://docs.python.org/3/library/random.html
import names #pip install names https://pypi.org/project/names/
import time
import datetime

def randInt(min,max): #min <= x <= max
    """! This function used to generate random Integer. 
    @param min smallest number can be generated
    @param max largest number can be generated
    @return number generated
    """
    return random.randint(min,max) #return a random int value

def randChance(perc): #generate a random percentage chance 
    """! This function used to generate random percentage value. 
    @param perc percentage
    @return True if succeed, False if failure
    """
    return (randInt(0,100) < perc) #return a random percentage

def randName(): #generates a random name
    """! This function used to generate random names 
    @return name
    """
    x = "female" if randInt(0,1) == 0 else "male" #determine the gender of the person, before assign a name
    return names.get_full_name(x) #returns person name

def random_date(start, end): #generates a random date 
    """! This function generates a random timestamp between start and end date
    @param start start is the start date
    @param end end is the end date
    @return timestamp
    """
    def str_time_prop(start, end, format, prop):
        """Get a time at a proportion of a range of two formatted times.

        start and end should be strings specifying times formated in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
        """
        stime = time.mktime(time.strptime(start, format))  #generates a start time
        etime = time.mktime(time.strptime(end, format))  #generates an end time

        ptime = stime + prop * (etime - stime)
        return time.strftime(format, time.localtime(ptime)) 
    prop = random.random()
    return str_time_prop(start, end, '%Y-%m-%d %I:%M:%S', prop)

def random_timestamp(x, today): #generates a random time
    """! This function used to generate random timestamp. 
    @param x total sets of timestamps to be generated
    @param today to forcefully generate a set of timestamp from today
    @return list of x pairs of timestamps
    """
    res = []
    today = datetime.date.today()
    frmt = '%Y-%m-%d %I:%M:%S'
    d = 1 if today else 7
    start = (today-datetime.timedelta(days=d)).strftime(frmt) 
    end = (today).strftime(frmt)

    for i in range(x): 
        one = random_date(start, end) #generate a timestamp
        one = datetime.datetime.strptime(one,frmt) #format
        two = one+datetime.timedelta(hours=16) #generate a second timestamp within the next 16 hours
        two = random_date(one.strftime(frmt), two.strftime(frmt)) 
        two = datetime.datetime.strptime(two, frmt)
        res.append([one,two]) #appending the values into res[] 
        end = one.strftime(frmt) #change end date to prevent overlaps
        if d == 1:
            d = 7
            start = (today-datetime.timedelta(days=d)).strftime(frmt) #change start date
    return res

