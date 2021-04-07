import datetime

# in this file stores the functions we need to compare trace together data


# function to check if timestamp coincides

def checkTimeStamp(setoftimestamps1,setoftimestamps2): # function to check if timestamp coincides
    # version 1
    results = []
    for timestamp in setoftimestamps1: #iterate through the first set of timestamps 
        results.append(setoftimestamps2[0] < timestamp < setoftimestamps2[1]) #appending the value into results[]
    for timestamp in setoftimestamps2: #iterate through the second set of timestamps 
        results.append(setoftimestamps1[0] < timestamp < setoftimestamps1[1]) #appending the value into results[]
        return True in results
        