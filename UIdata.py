import peopleData
import json

peopleEdge = {}
peopleEdge['edges']=[]
def createPeopleJson():
    peopleJson = {}
    peopleJson["nodes"] = []
    for x in peopleData.listOfPpl:
        peopleJson["nodes"].append({
            "id": x.name,
            "token": x.token,
            "tag": peopleData.personTag(x.persontags).name,
        })
    with open('people.json', 'w') as outfile:
        json.dump(peopleJson, outfile)
        json.dump(peopleEdge, outfile)

def addPeopleConnectJson(x):
    peopleEdge["edges"].append(x)

# def createPeopleConnectJson():
#     with open('peopleEdge.json', 'w') as outfile:
#         json.dump(peopleEdge, outfile)

def createJson():
    createPeopleJson()