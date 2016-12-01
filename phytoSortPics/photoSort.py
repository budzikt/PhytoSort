'''
Created on 30.11.2016

@author: Tomek
'''
import os
import re
import glob
from macpath import dirname
import shutil
dateFinder = re._compile('^([0-9]{8})', 0)

print(os.getcwd())
mypath = os.getcwd()
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.endswith(".jpg")]
nameList = []
for f in onlyfiles:
    matchObj = dateFinder.match(f)
    if matchObj != None:
        nameList.append(matchObj.group(0))
nameList = list(set(nameList))
#Uniques
#print(nameList)
nameDir = []
for index, fl in enumerate(nameList):
    nameDir.append(nameList[index][:4] + '_'+nameList[index][4:6]+'_'+nameList[index][6:8])
    if not os.path.exists(os.getcwd()+ "\\" + nameDir[index]):
        os.makedirs(os.getcwd()+ "\\" + nameDir[index])
    else:
        print("Directory " + nameDir[index] + " already exist")

for index, nl in enumerate(nameList):
    dateObjList = glob.glob(nl+"*")
    if dateObjList:
        for fileToCpy in dateObjList:
            filePath = os.getcwd()+ "\\" + fileToCpy
            destDirPath = os.getcwd()+ "\\" + nameDir[index] + "\\"
            if not os.path.exists(destDirPath + "\\" + fileToCpy):
                print("Copy " + fileToCpy + " to directory "+ destDirPath)
                shutil.copy2(filePath, destDirPath)
            else:
                print("File already exist")
    else:
        print("No pictures with date "+ nameDir[index] + " (names starts with "+ nl + ")")


    
