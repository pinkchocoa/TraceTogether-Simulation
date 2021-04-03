import randomFn

# in this file stores the functions we need to compare trace together data

# function to check if timestamp coincides
def checkTimeStamp():
    setoftimestamps1 = randomFn.random_timestamp(1, 1)[0]
    setoftimestamps2 = randomFn.random_timestamp(1, 1)[0]

    # print(setoftimestamps1[0], setoftimestamps1[1])
    # print(setoftimestamps2[0], setoftimestamps2[1])

    #version 1
    # results = []
    # for timestamp in setoftimestamps1:
    #     results.append(setoftimestamps2[0] < timestamp < setoftimestamps2[1])
    # for timestamp in setoftimestamps2:
    #     results.append(setoftimestamps1[0] < timestamp < setoftimestamps1[1])
    #     return True in results


    #version 2
    Intervals1 = [
        {'starting_time': '2021-04-04 07:10:39.286168', 'ending_time': '2021-04-04 07:10:40.276504'},
        {'starting_time': '2021-04-04 07:10:40.301116', 'ending_time': '2016-02-26 07:10:40.722193'},
    ]
    Intervals2 = [
        {'starting_time': '2021-04-04 07:10:39.590220', 'ending_time': '2021-04-04  07:10:41.482954'},
        {'starting_time': '2021-04-04 07:10:41.649375', 'ending_time': '2021-04-04 07:10:42.615738'},
    ]

    for i1, d1 in enumerate(Intervals1):
        for i2, d2 in enumerate(Intervals2):
            start1 = d1["starting_time"]
            start2 = d2["starting_time"]
            end1 = d1["ending_time"]
            end2 = d2["ending_time"]

            if end1 >= start2 and end2 >= start1:
                print("Intervals1", i1, "overlaps with Intervals2", i2)

    # print(setoftimestamps1[0], setoftimestamps1[1])
    # print(setoftimestamps2[0], setoftimestamps2[1])
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
