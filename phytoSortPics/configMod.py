'''
Created on 03.12.2016

@author: Tomek
'''
import re

regExPatterns = {'Samsung':'^([0-9]{8})',
                 'Generic':'^IMG_[0-9]{5}'}

def getMatcher(pattern):
    matcher = re._compile(regExPatterns[pattern], 0)
    return matcher

