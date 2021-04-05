import datetime

# in this file stores the functions we need to compare trace together data


# function to check if timestamp coincides

def checkTimeStamp(setoftimestamps1,setoftimestamps2):
    # version 1
    results = []
    for timestamp in setoftimestamps1:
        results.append(setoftimestamps2[0] < timestamp < setoftimestamps2[1])
    for timestamp in setoftimestamps2:
        results.append(setoftimestamps1[0] < timestamp < setoftimestamps1[1])
        return True in results

    # # ^i used the above to generate 2 random sets of timestamps,
    # # u can create ur own too for checking
    # # they should be datetime objects
    # print(setoftimestamps1)
    # print(setoftimestamps2)
    # ^this is how its like
    # the format of the object is frmt = '%Y-%m-%d %I:%M:%S'

    # check if timestamp coincides and return by how many minutes
    # return should be an integer

