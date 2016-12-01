'''
Created on 30.11.2016

@author: Tomek
'''
import os
import re
import glob
from macpath import dirname
import shutil

#To find Samsung-format string
dateFinder = re._compile('^([0-9]{8})', 0)

#get current working dir
mypath = os.getcwd()
#Generator expression to get only files and only jpeg-s
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.endswith(".jpg")]
nameList = []
for f in onlyfiles:
    #Pass pictures through regex checker
    matchObj = dateFinder.match(f)
    if matchObj != None:
        nameList.append(matchObj.group(0))
#Remove duplicates from file list
nameList = list(set(nameList))

nameDir = []
#generate nice folder names [yyyy-mm-dd]
for index, fl in enumerate(nameList):
    nameDir.append(nameList[index][:4] + '_'+nameList[index][4:6]+'_'+nameList[index][6:8])
    if not os.path.exists(os.path.join(os.getcwd(),nameDir[index])):
        os.makedirs(os.path.join(os.getcwd(), nameDir[index]))
    else:
        print("Directory " + nameDir[index] + " already exist")

#Serch for files that match time pattern of folder
for index, nl in enumerate(nameList):
    dateObjList = glob.glob(nl+"*")
    if dateObjList:
        for fileToCpy in dateObjList:
            filePath = os.path.join(os.getcwd(), fileToCpy)
            destDirPath = os.path.join(os.getcwd(), nameDir[index])
            if not os.path.exists(destDirPath + "\\" + fileToCpy):
                print("Copy " + fileToCpy + " to directory "+ destDirPath)
                shutil.copy2(filePath, destDirPath)
            else:
                print("File already exist")
    else:
        print("No pictures with date "+ nameDir[index] + " (names starts with "+ nl + ")")


    
