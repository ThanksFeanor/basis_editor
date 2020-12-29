import json
import datetime
import os
from presets import createPreset, readFromCustom

defaultbasis = '{"list":[],"current":0}'
backupFolderName = "bak"
def backupfilename():
    return datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+"_basis.json.bak"

def addCustomSet(IDMap,SetName="Custom Set",LUName="Custom Lineup"):
    #Open basis.json, or create an empty one if not found
    try:
        with open("basis.json","r",encoding="utf8") as openfile:
            text = openfile.read()
        #Save a backup of basis.json with current timestamp
        if os.path.isdir(backupFolderName) == False:
            os.mkdir(backupFolderName)
        with open(os.path.join(backupFolderName,backupfilename()),"w",encoding="utf8") as output:
            output.write(text)
    except:
         text = defaultbasis
         
    #Convert basis.json into a python-format dictionary    
    js = json.loads(text)
    
    #Create a new set of lineups, and add it to the list of sets
    newSet = {}
    js["list"].append(newSet)
    
    #Initialise name and treasures for set
    newSet["name"] = SetName
    newSet["t"] = {"tech":[30,30,30,30,30,30,30,10,30],
                   "trea":[300,300,300,300,300,300,600,600,600,300,300],
                   "bslv":[20,20,20,20,20,20,20,20],
                   "fruit":[300,300,300,300,300,300,300],
                   "gods":[100,100,100],
                   "alien":600,
                   "star":1500}
    newSet["sele"] = 0
    
    #Add a list of lineups to the set
    newLineUps = []
    newSet["lb"] = newLineUps
    
    #Add a lineup to the list of lineups
    newLineUp = {}
    newLineUps.append(newLineUp)
    
    #Initialise the name and nyc (cannon info idk?) of the new lineup
    newLineUp["name"] = LUName
    newLineUp["nyc"] = [0,0,0]
    
    #Create a data structure to describe the lineup and add it to the lineup
    lineUpData = {}
    newLineUp["lu"] = lineUpData
    
    #Cats assigned to the lineup
    lineUpData["fs"] = [[None]*5]*2
    
    #Mapping of cats to default levels
    levelMapping = []
    lineUpData["map"] = levelMapping
    
    #Given a dictionary of ID:level pairs, set up the default levels
    for i in IDMap:
        levelMapping.append(
            {
                'key': {'cls': 'common.util.unit.Unit', 'pack': '000000', 'id': i},
                'val': {'lvs': [IDMap[i], 0, 0, 0, 0, 0], 'orbs': None}
            }
            )
    
    #Edit basis.json with new shit
    out = json.dumps(js)
    with open("basis.json","w",encoding="utf8") as output:
        output.write(out)
    return js

def cleanSets():
    try:
        with open("basis.json","r",encoding="utf8") as openfile:
            text = openfile.read()
        #If text is not the empty basis, make a backup with current timestamp
        if text != defaultbasis:
            if os.path.isdir(backupFolderName) == False:
                os.mkdir(backupFolderName)
            with open(os.path.join(backupFolderName,backupfilename()),"w",encoding="utf8") as output:
                output.write(text)
    except:
        pass
    #Empty basis to have no sets
    with open("basis.json","w",encoding="utf8") as output:
        output.write(defaultbasis)
    
print("What action would you like to perform?")
print("1 : Add a set with preset levels based on rarity (e.g. normals 60, rares 30...)")
print("2 : Add a set with preset levels based on a provided tsv file")
print("3 : Clear all sets in the file")
response = -1
while response not in ["1","2","3"]:
    response = str(input("Select your option : "))

if response == "1":
    print("Select a preset")
    print("1 : Normals 40, Others 20")
    print("2 : Normals 60, Others 30")
    print("3 : Normals 80, Ubers/LRs 30, Others 40")
    print("4 : User Defined")
    response1 = -1
    while response1 not in ["1","2","3","4"]:
        response1 = str(input("Select your option : "))
elif response == "2":
    print("Give file name of your custom tsv")
    print("It should be in the same folder as this code and have IDs in first column, and levels in 5th")
    filename = input("Name : ")
    try:
        addCustomSet(readFromCustom(filename))
    except:
        print("File not found or other error occured")      
elif response == "3":
    cleanSets()
    print("All Sets Cleared. If this was undesired, then a backup has been saved in bak folder.")
else:
    print("Error")
    
if response == "1":    
    if response1 == "1":
        try:
            addCustomSet(createPreset([40,20,20,20,20,20]))
        except:
            print("Error occured")
    elif response1 == "2":
        try:
            addCustomSet(createPreset([60,30,30,30,30,30]))
        except:
            print("Error occured")
    elif response1 == "3":
        try:
            addCustomSet(createPreset([80,40,40,40,30,30]))
        except:
            print("Error occured")
    elif response1 == "4":
        print("Enter Desired Levels Of - ")
        userDefined = [30,30,30,30,30,30]
        userDefined[0] = int(input("Normals : "))
        userDefined[1] = int(input("Specials : "))
        userDefined[2] = int(input("Rares : "))
        userDefined[3] = int(input("Super Rares : "))
        userDefined[4] = int(input("Uber Super Rares : "))
        userDefined[5] = int(input("Legend Rares : "))
        try:
            addCustomSet(createPreset(userDefined))
        except:
            print("Error occured")