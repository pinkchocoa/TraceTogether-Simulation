import random #https://docs.python.org/3/library/random.html
import names #pip install names https://pypi.org/project/names/

def randInt(min,max): #min <= x <= max
    return random.randint(min,max)

def randName(): #generates a random name
    x = "female" if randInt(0,1) == 0 else "male"
    return names.get_full_name(x)