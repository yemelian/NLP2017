import sys,os
from os import listdir
from os.path import isfile, join
from collections import Counter
import numpy as np


def calculate_Unigrams():
    # Define paths to corpuses
    mypathENG = r'C:\Temp\NLP\testset_literature'
    mypathHEB = r'C:\Temp\NLP\haaretz.heb'
    filesENG = [f for f in listdir(mypathENG) if isfile(os.path.join(mypathENG, f))]
    filesHEB = [f for f in listdir(mypathHEB) if isfile(os.path.join(mypathHEB, f))]
    # unigrams - counter for all words in corpuses
    wordsTotal = 0
    #all of bigrams will be there in that var
    bigrams={}

    for name in filesENG:
        with open(mypathENG + '\\' + name, encoding="utf8") as f:
            words = [word for line in f for word in line.split()]
            # wordsTotal=wordsTotal+Counter(words)
            # Counting words for every file and su,,arize it with previous value - testset_literature
            wordsTotal = wordsTotal + len(words)

        #calculating Bigrams
        with open (mypathENG + '\\' + name, encoding="utf8") as myfile:
            data=myfile.readlines()
            newBigrams=[b for l in data for b in zip(l.split()[:-1], l.split()[1:])]

        for everyElement in newBigrams:
         if everyElement in bigrams.keys():
            bigrams[everyElement]+=1
         else:
            bigrams[everyElement]=0


    for name in filesHEB:
        with open(mypathHEB + '\\' + name, encoding="utf8") as f:
            words = [word for line in f for word in line.split()]
            # wordsTotal = wordsTotal + Counter(words)
            # Counting words for every file and su,,arize it with previous value - haaretz.heb
            wordsTotal = wordsTotal + len(words)

        #calculating Bigrams
        with open (mypathHEB + '\\' + name, encoding="utf8") as myfile2:
            data2=myfile2.readlines()
            newBigrams = [b for l in data2 for b in zip(l.split()[:-1], l.split()[1:])]
        for everyElement in newBigrams:
         if everyElement in bigrams.keys():
            bigrams[everyElement]+=1
         else:
            bigrams[everyElement]=0

    #unigrams - returns number of all words at all corpuses
    return wordsTotal
pass

if __name__ == "__main__":
    print(calculate_Unigrams())



