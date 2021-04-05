import peopleData
import json
import randomFn

peopleJson = {}
peopleJson["nodes"]=[]
peopleJson["edges"]=[]
def createPeopleJson():
    for x in peopleData.listOfPpl:
        peopleJson["nodes"].append({
            "id": x.name,
            #"token": x.token,
            "group": x.persontags,
            #"x": randomFn.randInt(1,300),
            #"y": randomFn.randInt(1,300)
        })
    with open('people.json', 'w') as outfile:
        json.dump(peopleJson, outfile)

def addPeopleConnectJson(x):
    peopleJson["edges"].append(x)

# def createPeopleConnectJson():
#     with open('peopleEdge.json', 'w') as outfile:
#         json.dump(peopleEdge, outfile)

def createJson():
    createPeopleJson()