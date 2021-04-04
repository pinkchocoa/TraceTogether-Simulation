import randomFn

# in this file stores the functions we need to compare trace together data


# function to check if timestamp coincides
def checkTimeStamp():
    setoftimestamps1 = randomFn.random_timestamp(1, 1)[0]
    setoftimestamps2 = randomFn.random_timestamp(1, 1)[0]

    print(setoftimestamps1[0], setoftimestamps1[1])
    print(setoftimestamps2[0], setoftimestamps2[1])

    # version 1
    results = []
    for timestamp in setoftimestamps1:
        results.append(setoftimestamps2[0] < timestamp < setoftimestamps2[1])
    for timestamp in setoftimestamps2:
        results.append(setoftimestamps1[0] < timestamp < setoftimestamps1[1])
        return True in results

    # version 2
    # person1 = [
    #     {'check_in_time': setoftimestamps1[0], 'check_out_time': setoftimestamps1[1]},
    # ]
    # person2 = [
    #     {'check_in_time': setoftimestamps2[0], 'check_out_time': setoftimestamps2[1]},
    # ]
    #
    # for i1, d1 in enumerate(person1):
    #     for i2, d2 in enumerate(person2):
    #         start1 = d1["check_in_time"]
    #         start2 = d2["check_in_time"]
    #         end1 = d1["check_out_time"]
    #         end2 = d2["check_out_time"]
    #
    #         if start2 >= start1 and end2 >= end1:
    #             print("person1", i1, "overlaps with person2", i2)

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
