import sys,os
from os import listdir
from os.path import isfile, join
from collections import Counter
import numpy as np


def calculate_Unigrams():
    # Define paths to corpuses
    mypathENG = r'C:\Users\uckpa\Documents\University 2016\NLanguages\NLP2017\testset_literature'
    mypathHEB = r'C:\Users\uckpa\Documents\University 2016\NLanguages\NLP2017\haaretz.heb'
    filesENG = [f for f in listdir(mypathENG) if isfile(os.path.join(mypathENG, f))]
    filesHEB = [f for f in listdir(mypathHEB) if isfile(os.path.join(mypathHEB, f))]
    # Init counter for words
    # wordsTotal=Counter()
    wordsTotal = 0
    for name in filesENG:
        with open(mypathENG + '\\' + name, encoding="utf8") as f:
            words = [word for line in f for word in line.split()]
            # wordsTotal=wordsTotal+Counter(words)
            # Counting words for every file and su,,arize it with previous value - testset_literature
            wordsTotal = wordsTotal + len(words)

    for name in filesHEB:
        with open(mypathHEB + '\\' + name, encoding="utf8") as f:
            words = [word for line in f for word in line.split()]
            # wordsTotal = wordsTotal + Counter(words)
            # Counting words for every file and su,,arize it with previous value - haaretz.heb
            wordsTotal = wordsTotal + len(words)
    #returns number of all words at all corpuses
    return wordsTotal
    pass

if __name__ == "__main__":
    print(calculate_Unigrams())



