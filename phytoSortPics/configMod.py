'''
Created on 03.12.2016

@author: Tomek
'''
import re

regExPatterns = {'Samsung':['^([0-9]{8}).*','^([0-9]{4})([0-9]{2})([0-9]{2})','y m d'],
                 'Generic':'^IMG_[0-9]{5}'}

def getFileMatcher(pattern):
    matcher = re._compile(regExPatterns[pattern][0], 0)
    return matcher

def getFolderMatcher(pattern):
    folderName = re.compile(regExPatterns[pattern][1], 0)
    return folderName

def getFolderTags(pattern):
    folderTags = str.split(' ', regExPatterns[pattern][2])
    return folderTags

