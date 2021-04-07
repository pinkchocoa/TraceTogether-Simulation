import random

def file_to_2dlist(file_name):
    """! This method reads a file and convert each line to list items
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
    return random.randint(min,max)

def randChance(perc):
    return (randInt(0,100) < perc)