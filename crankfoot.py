#!/usr/bin/env python

# Name:      crankfoot.py
# Authors:   Michael Albert, Matthew Sheridan
# Date:      22 April 2016
# Revision:  23 April 2016
# Description:
#   CRANKFOOT
#
#   Don't know what that means?
#   Get the hell out of here.

"""CRANKFOOT"""

__authors__ = "Michael Albert, Matthew Sheridan"
__credits__ = ["Michael Albert, Matthew Sheridan"]
__date__    = "22 April 2016"
__version__ = "0.1"
__status__  = "Development"

import os
import random

#Global variables
ALLWORDS = ""
RELWORDS = ""
X = 10
Q = 20

def random_event(anti = 0):
    if random.randrange(100) <= (X+anti):
        return True
    return False

def quirky_prefix(word):
    '''Returns a quirky (pronouncable) prefix to preceed a word.'''

    return prefixed

def quirky_suffix(word):
    '''Returns a quirky (pronouncable) suffix to append to a word.'''

    suffix = ""

    return suffixed

def mashable(word1, word2):
    '''Returns true if the two words can be audibly combined.'''

    if (word1[-1] == word2[0]):
        return True

    for i in range(len(word1)-1):
        if (word1[i] == word2[0]) and (word1[i+1] == word2[-1]):
                return True
    
    return False

def mash_left(word1, word2):
    '''Pushes word1 into word2 from the left'''

    if not word1:
        return word2
    if not word2:
        return word1
    
    for i in range(len(word1)):
        lastchars = word1[len(word1) - (i+1):]
        if i < len(word2):
            firstchars = word2[:i+1]
            if lastchars == firstchars:
                return word1 + word2[len(lastchars):]
    return ""

def mash_left_count(word1, word2):
    '''Returns number of characters that would overlap by calling mash_left(word1, word2).'''
    
    for i in range(len(word1)):
        lastchars = word1[len(word1) - (i+1):]
        if i < len(word2):
            firstchars = word2[:i+1]
            if lastchars == firstchars:
                return len(lastchars)
    return 0

def mash_right(word1, word2):
    '''Pushes word1 into word2 from the right.'''
    
    return mash_left(word2, word1)

def mash_mid(word1, word2):
    '''Tries to mash word2 into arbitrary positions within word1. Does not care
       about edges of word1; that can be taken care of with mash_left.
       Returns a list of mashed words.'''

    mashes = []

    for i in range(len(word1)):
        word1_left = word1[:i+1]
        word1_right = word1[i+1:]
        overlap_left = mash_left_count(word1_left, word2)
        overlap_right = mash_left_count(word2, word1_right)
        if overlap_left > 0 and overlap_right > 0:
            pair = word2[:overlap_left] + word2[-overlap_right:]
            word1_split = word1.split(pair, maxsplit=1)
            mashes.append(str(word1_split[0]) + word2 + str(word1_split[1]))

    return mashes

def mash(word1, word2):
    '''Pre-condition: word1 and word2 are "mashable"
          Returns the mashed words'''

    newwords = []

    for i in range(len(word1)):
        word1left = word1[:i+1]
        word1right = word1[i+1:]
        leftpush = mash_left(word1left, word2)
        if leftpush:
            delta = len(word1left) + len(word2) - len(leftpush)
            leftpush2 = mash_left(word2[delta:], word1right)
            if leftpush2:
                newwords.append(word1left+leftpush2)
    return newwords
    
def genpuns(word):
    '''Returns a list of pun words using the word given.'''

    puns = []

    for term in RELWORDS:
        
        workingset = []
        
        if mashable(word, term):
            mashed = mash(word, term)
            for amash in mashed:
                if random_event():
                    amash = quirky_suffix(amash)
                    if random_event():
                        amash = quirky_prefix(word)
                    puns.append(amash)
            puns += mashed

        if mashable(term, word):
            mashed = mash(term, word)
            for amash in mashed:
                if random_event():
                    amash = quirky_suffix(amash)
                    if random_event():
                        amash = quirky_prefix(word)
                    puns.append(amash)
            puns += mashed

    for a in range(X):
        if random_event():
            quirked = quirky_suffix(word)
            if random_event():
                quirked = quirky_prefix(quirked)
            puns.append(quirked)
    
    return puns

def punnify(keywords):
    '''Creates and returns a set of funny pun words from the two input word sets.'''

    puns = []

    for word in keywords:
        puns += genpuns(word)

    return puns
