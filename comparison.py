import datetime

# function to check if timestamp coincides
def checkTimeStamp(setoftimestamps1,setoftimestamps2):
    results = []
    for timestamp in setoftimestamps1: 
        results.append(setoftimestamps2[0] < timestamp < setoftimestamps2[1]) 
    for timestamp in setoftimestamps2: 
        results.append(setoftimestamps1[0] < timestamp < setoftimestamps1[1]) 
        return True in results
        