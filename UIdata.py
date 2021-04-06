import peopleData
import json
import randomFn

peopleJson = {}
peopleJson["nodes"]=[]
peopleJson["edges"]=[]

tagJson = {}
tagJson[peopleData.personTag(0).name]=0
tagJson[peopleData.personTag(1).name]=0
tagJson[peopleData.personTag(3).name]=0

def createPeopleJson():
    for x in peopleData.listOfPpl:
        peopleJson["nodes"].append({
            "id": x.name,
            #"token": x.token,
            "group": peopleData.personTag(x.persontags).name,
            #"x": randomFn.randInt(1,300),
            #"y": randomFn.randInt(1,300)
        })
        tagJson[peopleData.personTag(x.persontags).name]+=1
    with open('people.json', 'w') as outfile:
        json.dump(peopleJson, outfile)
    with open('tag.json', 'w') as outfile:
        json.dump(tagJson, outfile)

def addPeopleConnectJson(x):
    peopleJson["edges"].append(x)

# def createPeopleConnectJson():
#     with open('peopleEdge.json', 'w') as outfile:
#         json.dump(peopleEdge, outfile)


def createJson():
    createPeopleJson()