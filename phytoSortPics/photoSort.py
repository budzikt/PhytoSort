'''
Created on 30.11.2016

@author: Tomek
'''
import os
import re
import glob
import shutil
import unittest
import argparse
import sys

regExPatterns = {'Samsung':'^([0-9]{8})'}

#To find Samsung-format string
dateFinder = re._compile(regExPatterns['Samsung'], 0)

def pictureOrder():
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

def IsOdd(n):
    return n % 2 == 1
# TESTS 
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(IsOdd(1))

    def testTwo(self):
        self.assertFalse(IsOdd(2))


def mainTest():
    unittest.main()
    
#RUN as script
if __name__ == "__main__":
    print("\n\n***RUN***\nRun as script with arglist:")
    print(sys.argv)
    #Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('--tr', '-tr',  action='store_true')
    args =parser.parse_args(sys.argv)
    
    print(args)
    #Test suite goes here
    try:
        if sys.argv[1] == 'testRun':
            mainTest()
    except IndexError:
        print('No test running')  
    
    
    