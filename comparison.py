## @file comparison.py
#
# @brief this file checks if timestamp conincides 
#


#library imporst
import datetime


def checkTimeStamp(setoftimestamps1,setoftimestamps2):
    """!checkTimeStamp method checks if the timestamp conincides
    @param setoftimestamps1, setoftimestamps2 
    @return True/False 
    """
    results = []
    for timestamp in setoftimestamps1: 
        results.append(setoftimestamps2[0] < timestamp < setoftimestamps2[1]) 
    for timestamp in setoftimestamps2: 
        results.append(setoftimestamps1[0] < timestamp < setoftimestamps1[1]) 
        return True in results
        