#encoding: utf-8
'''
Created on Oct 22, 2014

@author: tmahrt

Basic examples of common usage.
'''

from pysle import isletool
from pysle import pronunciationtools

# In this first example we look up the syllabification of a word and get it's 
# stress information.

searchWord = 'catatonic'
isleDict = isletool.LexicalTool('ISLEdict.txt')
lookupResults = isleDict.lookup(searchWord)

firstEntry = lookupResults[0]
firstSyllableList = firstEntry[0] 
firstSyllableList = ".".join([u" ".join(syllable) for syllable in firstSyllableList])
firstStressList = firstEntry[1]

print(searchWord)
print(firstSyllableList)
print(firstStressList) # 3rd syllable carries stress


# Here we determine the syllabification of a word, as it was said.
# (Of course, this is just a guess)
print('-'*50)

searchWord = 'another'
anotherPhoneList = ['n', '@', 'th', 'r']

returnList = pronunciationtools.findBestSyllabification(isleDict, 
                                                        searchWord, 
                                                        anotherPhoneList)

(stressedSyllable, syllableList, syllabification,
stressedSyllableIndexList, stressedPhoneIndexList,
flattenedStressIndexList) = returnList
print(searchWord)
print(anotherPhoneList)
print(stressedSyllableIndexList) # We can see the first syllable was elided
print(stressedPhoneIndexList)
print(flattenedStressIndexList)
print(syllableList)
print(syllabification)

