import datetime

# in this file stores the functions we need to compare trace together data


# function to check if timestamp coincides
def checkTimeStamp():
    setoftimestamps1=[]
    setoftimestamps2=[]

    setoftimestamps1.append(datetime.datetime(2020, 4, 4, 11, 30, 00))
    setoftimestamps1.append(datetime.datetime(2020, 4, 4, 18, 30, 00))
    setoftimestamps2.append(datetime.datetime(2020, 4, 4, 10, 30, 00))
    setoftimestamps2.append(datetime.datetime(2020, 4, 4, 20, 30, 00))

    print(setoftimestamps1[0], setoftimestamps1[1])
    print(setoftimestamps2[0], setoftimestamps2[1])

    results = []
    for timestamp in setoftimestamps1:
        if setoftimestamps2[0] < timestamp < setoftimestamps2[1]:
            results.append(timestamp)
    for timestamp in setoftimestamps2:
        if setoftimestamps1[0] < timestamp < setoftimestamps1[1]:
            results.append(timestamp)

    timeDiff = 0
    if len(results) == 0:
        return timeDiff
    else:
        if results[0] > results[1]:
            timeDiff = results[0] - results[1]
            timeDiff = timeDiff.total_seconds()/60
        else:
            timeDiff = results[1] - results[0]
            timeDiff = timeDiff.total_seconds()/60

    # for result in results:
    #     print(str(result))
    return timeDiff

    # # ^i used the above to generate 2 random sets of timestamps,
    # # u can create ur own too for checking
    # # they should be datetime objects
    # print(setoftimestamps1)
    # print(setoftimestamps2)
    # ^this is how its like
    # the format of the object is frmt = '%Y-%m-%d %I:%M:%S'

    # check if timestamp coincides and return by how many minutes
    # return should be an integer


print(checkTimeStamp())