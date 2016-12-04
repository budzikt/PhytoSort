'''
Created on 30.11.2016

@author: Tomek
'''
import os
import glob
import shutil
import unittest
import argparse
import sys
#Local Imports
import phytoSortPics.configMod  as cfg 

def pictureOrder():
    #get current working dir
    mypath = os.getcwd()
    onlyfiles = Ps_getFilesWithExt(mypath, 'jpg')
    dataMatcherRegex = cfg.getMatcher('Samsung')
    nameList = []
    for f in onlyfiles:
        #Pass pictures through regex checker
        matchObj = dataMatcherRegex.match(f)
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

def Ps_getFilesWithExt(mypath, ext):
    #Generator expression to get only files and only jpeg-s
    retList = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.endswith("."+ext)]
    return retList

#TESTS TESTS TESTS TESTS
class IsOddTests(unittest.TestCase):

    def testNameParse(self):
        myTestPath = os.path.join(os.getcwd(),'TestCases')
        testList = Ps_getFilesWithExt(myTestPath, 'jpg')
        self.assertNotEqual(len(testList), 0)
    
    def testMatchSamsung(self): 
        testName = '20161004_063218.jpg'  
        match = cfg.getMatcher('Samsung')
        match.match(testName)
        self.assertNotEqual(match, None)

def parseCmdArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-tr', '-testrun', '-TestRun', action='store_true', dest='tr')
    args = parser.parse_args(sys.argv)
    return vars(args)
    
def testNeeded(argsDict):
    if 'tr' in argsDict and argsDict['tr'] == True:
        return True
    else:
        return False

#Manage argvars to run unittests      
def mainTest():
    argsTemp = list(sys.argv)
    del sys.argv[1:]
    unittest.main()
    sys.argv = argsTemp
    
#RUN as script
if __name__ == "__main__":
    print("\n\n***RUN AS MAIN***\nRun as script with arglist: " + '\n' + str(sys.argv))
    #Parse command line arguments
    argMap = parseCmdArgs()
    if(testNeeded(argMap)):
        print('Run Unit Tests')
        mainTest()
    else:
        print('No test running')  
    pictureOrder()
    
    