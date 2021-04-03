from enum import Enum #https://www.tutorialspoint.com/enum-support-for-enumerations-in-python
import multidict #pip install multidict https://pypi.org/project/multidict/
import randomFn


class personTag(Enum):
    nothing = 0
    covid = 1
    closeWarning = 2

class person:
        def __init__(self,token,name,phoneNumber):
                super().__init__()
                self.token=token #identification
                self.name=name #IC number as the name
                self.phoneNumber=phoneNumber #Phone number with 8 digits
                #self.email=email
                self.persontags=personTag.nothing.value
                
                #data structs
                self.btsignal = set()
                self.location = multidict.MultiDict() #allows multiple keys
                self.btcount=0 #-The number of bluetooth signal made

        def print(self):
            print("token:", self.token)
            print("name:", self.name)
            print("phone number:", self.phoneNumber)
            print("tag:", personTag(self.persontags).name)


        


# listOfPpl = list()
# def generatePeople(x):
#     for id in range(x):
#         listOfPpl.append(person(id, randomFn.randName(),randomFn.randInt(80000000,99999998)))

# generatePeople(5)
# for x in listOfPpl:
#     x.print()