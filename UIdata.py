import peopleData
import json
import randomFn
import multidict

peopleJson = {}
peopleJson["nodes"]=[]
peopleJson["edges"]=[]

tagJson = {}
tagJson["overall"]=[]
# tagJson[peopleData.personTag(0).name]=0
# tagJson[peopleData.personTag(1).name]=0
# tagJson[peopleData.personTag(2).name]=0
# tagJson[peopleData.personTag(3).name]=0
peopleDetails = {}
peopleDetails["details"]=[]

def createPeopleJson():
    temp={}
    temp[peopleData.personTag(0).name]=0
    temp[peopleData.personTag(1).name]=0
    temp[peopleData.personTag(2).name]=0
    temp[peopleData.personTag(3).name]=0
    for x in peopleData.listOfPpl:
        temp[peopleData.personTag(x.persontags).name]+=1
        peopleDetails["details"].append({
            "id": x.name,
            "group": peopleData.personTag(x.persontags).name,
            "location": list(x.location.keys())
        })
        if x.persontags == peopleData.personTag.nothing.value:
            continue
        peopleJson["nodes"].append({
            "id": x.name,
            #"token": x.token,
            "group": peopleData.personTag(x.persontags).name,
            #"x": randomFn.randInt(1,300),
            #"y": randomFn.randInt(1,300)
        })
    tagJson["overall"].append({
        peopleData.personTag(0).name: temp[peopleData.personTag(0).name],
        peopleData.personTag(1).name: temp[peopleData.personTag(1).name],
        peopleData.personTag(2).name: temp[peopleData.personTag(2).name],
        peopleData.personTag(3).name: temp[peopleData.personTag(3).name]
    })
    with open('people.json', 'w') as outfile:
        json.dump(peopleJson, outfile)
    with open('tag.json', 'w') as outfile:
        json.dump(tagJson, outfile)
    with open('peopleDetails.json', 'w') as outfile:
        json.dump(peopleDetails, outfile)

def addPeopleConnectJson(x):
    peopleJson["edges"].append(x)

# def createPeopleConnectJson():
#     with open('peopleEdge.json', 'w') as outfile:
#         json.dump(peopleEdge, outfile)


def createJson():
    createPeopleJson()