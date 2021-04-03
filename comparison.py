import randomFn
#in this file stores the functions we need to compare trace together data

#function to check if timestamp coincides
def checkTimeStamp():
    setoftimestamps1 = randomFn.random_timestamp(1, 1)[0]
    setoftimestamps2 = randomFn.random_timestamp(1, 1)[0]
    print(setoftimestamps1[0], setoftimestamps1[1])
    print(setoftimestamps2[0], setoftimestamps2[1])
    #^i used the above to generate 2 random sets of timestamps,
    #u can create ur own too for checking
    #they should be datetime objects
    print(setoftimestamps1)
    #^this is how its like
    #the format of the object is frmt = '%Y-%m-%d %I:%M:%S'

    #check if timestamp coincides and return by how many minutes
    #return should be an integer


print(checkTimeStamp())