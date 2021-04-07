import peopleData
import json
import randomFn
import multidict

peopleJson = {}
peopleJson["nodes"]=[]
peopleJson["edges"]=[]

tagJson = {}
tagJson["overall"]=[]

peopleDetails = {}
peopleDetails["details"]=[]

tableJson = {}
tableJson["rank"] = []
tableJson["chart"] = []

traceInfo = {}
traceInfo["info"] = []

def createPeopleJson():
    temp={}
    temp[peopleData.personTag(0).name]=0
    temp[peopleData.personTag(1).name]=0
    temp[peopleData.personTag(2).name]=0
    temp[peopleData.personTag(3).name]=0
    mid = -250
    for x in peopleData.listOfPpl:
        temp[peopleData.personTag(x.persontags).name]+=1
        traceInfo["info"].append({
            "id": x.name,
            "phoneNum": x.phoneNumber,
            "group": peopleData.personTag(x.persontags).name,
            "location": list(x.location.keys())
            })

        if x.persontags == peopleData.personTag.nothing.value:
            continue
        if x.persontags == peopleData.personTag.covid.value:
            xCoord = mid # -250, 250
            yCoord = randomFn.randInt(-150,150)
            mid+=90
            peopleDetails["details"].append({
            "id": x.name,
            "group": peopleData.personTag(x.persontags).name,
            "location": list(x.location.keys())
            })
        elif x.persontags == peopleData.personTag.locationWarning.value:
            xCoord = randomFn.randInt(-750,-350)
            yCoord = randomFn.randInt(-350,350)
        else: #closeWarning
            xCoord = randomFn.randInt(350,750)
            yCoord = randomFn.randInt(-350,350)

        peopleJson["nodes"].append({
            "id": x.name,
            #"token": x.token,
            "group": peopleData.personTag(x.persontags).name,
            "x": xCoord,
            "y": yCoord
        })
        
    tagJson["overall"].append({
        peopleData.personTag(0).name: temp[peopleData.personTag(0).name],
        peopleData.personTag(1).name: temp[peopleData.personTag(1).name],
        peopleData.personTag(2).name: temp[peopleData.personTag(2).name],
        peopleData.personTag(3).name: temp[peopleData.personTag(3).name]
    })
    with open('website/json/people.json', 'w') as outfile:
        json.dump(peopleJson, outfile)
    with open('website/json/tag.json', 'w') as outfile:
        json.dump(tagJson, outfile)
    with open('website/json/peopleDetails.json', 'w') as outfile:
        json.dump(peopleDetails, outfile)
    with open('website/json/traceInfo.json', 'w') as outfile:
        json.dump(traceInfo, outfile)

def addPeopleConnectJson(x):
    peopleJson["edges"].append(x)

def createTableJson():
    for k,v in peopleData.covidLoc.items():
        tableJson["rank"].append({
            "mall": k,
            "covidCount": v,
            "crowdCount": len(peopleData.listOfPplPerLoc[k]) #numbner of unique check in over 7 days
        })
        if v != 0:
            tableJson["chart"].append({
                "mall": k,
                "covidCount": v
            })
    with open('website/json/table.json', 'w') as outfile:
        json.dump(tableJson, outfile)


def createJson():
    createPeopleJson()
    createTableJson()