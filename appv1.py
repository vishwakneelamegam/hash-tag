import re

#To find the tagged words in the given text
def findHash(text):
    try:
       return [op.replace('#','',1) for op in re.findall("[#]\w+", text)]
    except:
       return []

#To read the tagged words
def readHash(id):
    try:
       inF = open(str(id) + ".tag", "r+")
       return inF.read().splitlines()
    except Exception as e:
       print(e)
       return []

#To write the tagged words
def writeHash(id,hashList):
    try:
       outF = open(str(id) + ".tag", "a")
       outF.writelines(hashList)
       outF.close()
       return True
    except:
       return False

def mainApp(id,text):
    repo = readHash(id)
    tags = findHash(text)
    newTag = list(set(tags) - set(repo))
    writeHash(id,newTag)
    oldTag = list(set(text.split(" ")) & set(repo))
    return oldTag + tags

print(mainApp("vish1998","bmw"))
