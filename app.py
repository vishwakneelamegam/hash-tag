import re

#To find the tagged words in the given text
def findHash(text):
    try:
       return [op.replace('#','',1)+"\n" for op in re.findall("[#]\w+", text)]
    except:
       return []

#To read the tagged words
def readHash(id):
    try:
       inF = open(str(id) + ".tag", "r+")
       return inF.readlines()
    except:
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
    hash = findHash(text)
    print(repo)
    print(hash)
    print(writeHash(id,list(set(hash) - set(repo))))

mainApp("vish1998","ford and #ferrari")
