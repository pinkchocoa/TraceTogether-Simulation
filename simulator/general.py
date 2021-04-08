## @file general.py
#
# @brief this file contains the general functions used for filo i/o purposes
#
# @author Jodie
#
# @section libraries_main Libraries/Modules
# - random
#   - to generate random numbers

import random #to generate random numbers

def file_to_2dlist(file_name):
    """! This method reads a file and convert each line to a 2d list
    @param file_name file name
    @return 2d list with the file data
    """
    results = []
    with open(file_name, 'rt', encoding="utf-8") as f:
        for line in f:
            res=[]
            for x in line:
                if x != '\n' and x != ' ':
                    res.append(int(x))
            results.append(res)
    return results

def randInt(min,max): #min <= x <= max
    """! This function used to generate random Integer. 
    @param min smallest number can be generated
    @param max largest number can be generated
    """
    return random.randint(min,max)

def randChance(perc):
    """! This function used to generate random percentage value. 
    @param perc percentage
    """
    return (randInt(0,100) < perc)