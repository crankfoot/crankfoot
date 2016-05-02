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
KEYWORDS = ""
X = 10
Q = 0
vowels = ["a","e","i","o","u"]
cons = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
prondict = {"a": ["y","e|c|"]+cons, "a|c|":cons, "b":["b|v|","l|v|","r|v|", "s|v|", "w|v|"]+vowels, "b|v|":vowels, "c": ["h|v|","k","t|v|"]+vowels,
 "c|v|":vowels, "d":["d|v|","l|v|", "r|v|", "w|v|"]+vowels, "d|v|": vowels, "e": ["e|c|", "a|c|", "i|c|", "o|c|", "y"]+cons, "e|c|":cons,
    "f":["f|v|","l|v|","r|v|","w|v|"]+vowels, "f|v|":vowels, "g":["g|v|","h|v|","l|v|","r|v|","w|v|"]+vowels, "g|v|": vowels, "h":vowels, "h|v|": vowels,
        "i":["a|c|","e|c|","o|c|","u|c|"]+cons, "i|c|": cons, "j": vowels, "j|v|": vowels, "k":["l|v|","n|v|","r|v|","t|v|","w|v|"]+vowels, "k|v|": vowels,
            "l":["d|v|","f|v|","g|v|","k|v|","l|v|","m|v|","n|v|","p|v|","s|v|","t|v|","z|v|"]+vowels, "l|v|":vowels, "m":["n|v|","s|v|"]+vowels,
                "m|v|":vowels, "n":["g|v|", "k|v|", "s|v|", "t|v|", "x|v|"]+vowels, "n|v|":vowels, "o":["a|c|", "e|c|", "o|c|", "u|c|", "y"]+cons,
                    "o|c|":cons, "p":["f|v|", "h|v|", "l|v|", "p|v|", "r|v|", "s|v|", "t|v|", "w|v|"]+vowels, "p|v|":cons, "q":["u"],
                        "r":["b|v|","c|v|","d|v|","f|v|","g|v|","k|v|","l|v|","m|v|","n","p|v|","q","r|v|","s|v|", "t|v|", "x|v|", "z|v|"]+vowels,
                            "r|v|":vowels,"s":["c|v|","h|v|","k|v|","l|v|","m|v|","n|v|","p|v|", "q", "s|v|", "t|v|", "w|v|"]+vowels, "s|v|":vowels,
                                "t":["h|v|","r|v|","t|v|","w|v|","z|v|"]+vowels, "t|v|":vowels, "u":["a|c|","e|c|","i|c|","o|c|","y"]+cons, "u|c|":cons,
                                    "v":["r|v|"]+vowels, "v|v|":vowels, "w":["h|v|", "r|v|","s|v|","t|v|","z|v|"]+vowels, "w|v|":vowels, "x":["x|v|"]+vowels,
                                        "x|v|":vowels, "y":["a", "e", "i", "o", "u"], "z":["h|v|","l|v|","w|v|","z|v|"]+vowels, "z|v|":vowels}

def random_event(anti = 0):
    if random.randrange(100) <= (X+anti):
        return True
    return False

def quirky_prefix(word):
    '''Returns a quirky (pronouncable) prefix to preceed a word.'''
    
    return word

def quirky_suffix(word):
    '''Returns a quirky (pronouncable) suffix to append to a word.'''

    suffixed = ""
    suffix =[]
    c = 0

    if word[-1] in cons:
        suffix.append(random.choice(vowels))
    elif word[-1] in vowels:
        suffix.append(random.choice(cons))
    else:
        suffix.append(random.choice(prondict["y"]))
        
    while random.randrange(100) <= Q:
        suffix.append(random.choice(prondict[suffix[c]]))
        c += 1

    for l in suffix:
        suffixed += l[0]

    return mash_left(word, suffixed)

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
    return word1+word2

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
        if (leftpush!=word1left+word2):
            delta = len(word1left) + len(word2) - len(leftpush)
            leftpush2 = mash_left(word2[delta:], word1right)
            if (leftpush2!=word2[delta:]+word1right):
                newwords.append(word1left+leftpush2)
    return newwords
    
def genpuns(word):
    '''Returns a list of pun words using the word given.'''

    puns = []

    for term in RELWORDS:
        
        workingset = []
        
        mashed = mash(word, term)
        for amash in mashed:
            if random_event():
                amash = quirky_suffix(amash)
                if random_event():
                    amash = quirky_prefix(word)
                puns.append(amash)
        puns += mashed

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

def load_words(kwdfilename, rwdfilename):
    '''Loads the keywords from the file "kwdfilename" and relevant words from "rwdfilename"'''

    global KEYWORDS
    global RELWORDS

    with open(kwdfilename, "r") as myfile:
        KEYWORDS=myfile.read()
        KEYWORDS = KEYWORDS.replace(' ', '').lower().split("\n")
    with open(rwdfilename, "r") as myfile:
        RELWORDS=myfile.read()
        RELWORDS = RELWORDS.replace(' ', '').lower().split("\n")

def punnify():
    '''Creates and returns a set of funny pun words from the two input word sets.'''

    puns = []

    for word in KEYWORDS:
        if word:
            puns += genpuns(word)

    return puns

def main():
    
    load_words("list_words","list_words")
    #print("KWD: "+str(KEYWORDS)+" RWD: "+str(RELWORDS))
    puns = punnify()
    unique_puns = set()
    for p in puns:
        unique_puns.add(p)
    for p in unique_puns:
        print(p)
        input()

if __name__ == '__main__':
    main()
