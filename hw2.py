import sys,os,math
from os import listdir
from os.path import isfile, join
from collections import Counter
import numpy as np

bigrams={}  #all of bigrams will be there in that var
frequencyOfEachWord={}
pmiResults={}
wordsTotal=0 # unigrams - counter for all words in corpuses

def calculatePMI(): #PMI(x,y) = log(P(xy)/P(x)*P(y) * 1000
 global pmiResults
 global wordsTotal

 for everyElement in bigrams:
   Pxy=bigrams[everyElement]
   Px=frequencyOfEachWord[everyElement[0]]
   Py=frequencyOfEachWord[everyElement[1]]
   PMI=math.log((Pxy/Px*Py),2)*1000/wordsTotal
   pmiResults[everyElement]=PMI

def calculate_Unigrams(argv):
    global bigrams
    global frequencyOfEachWord
    global wordsTotal
    # Define paths to corpuses: sys.argv[1] = r'C:\Temp\NLP\testset_literature' sys.argv[2] = r'C:\Temp\NLP\haaretz.heb'
    filesENG = [f for f in listdir(sys.argv[1]) if isfile(os.path.join(sys.argv[1], f))]
    filesHEB = [f for f in listdir(sys.argv[2]) if isfile(os.path.join(sys.argv[2], f))]

    for name in filesENG:
        with open(sys.argv[1] + '\\' + name, encoding="utf8") as f:
            words = [word for line in f for word in line.split()]
            # wordsTotal=wordsTotal+Counter(words)
            # Counting words for every file and su,,arize it with previous value - testset_literature
            wordsTotal = wordsTotal + len(words)

        #Calculating P(word) - frequency at corpus - START
        for everyElement in words:
         if everyElement in frequencyOfEachWord.keys():
            frequencyOfEachWord[everyElement]+=1
         else:
            frequencyOfEachWord[everyElement]=1
        #Calculating P(word) - frequency at corpus - END

        #calculating Bigrams P(word1, word2) in ENG start
        with open (sys.argv[1] + '\\' + name, encoding="utf8") as myfile:
            data=myfile.readlines()
            newBigrams=[b for l in data for b in zip(l.split()[:-1], l.split()[1:])]
        #Bigram adding
        for everyElement in newBigrams:
         if everyElement in bigrams.keys():
            bigrams[everyElement]+=1
         else:
            bigrams[everyElement]=1

     #calculating Bigrams in HEB start
    for name in filesHEB:
        with open(sys.argv[2] + '\\' + name, encoding="utf8") as f:
            words = [word for line in f for word in line.split()]
            # wordsTotal = wordsTotal + Counter(words)
            # Counting words for every file and su,,arize it with previous value - haaretz.heb
            wordsTotal = wordsTotal + len(words)

        #Calculating P(word) - frequency at corpus - START
        for everyElement in words:
         if everyElement in frequencyOfEachWord.keys():
            frequencyOfEachWord[everyElement]+=1
         else:
            frequencyOfEachWord[everyElement]=1
        #Calculating P(word) - frequency at corpus - END

        #calculating Bigrams P(word1, word2) in HEB start
        with open (sys.argv[2] + '\\' + name, encoding="utf8") as myfile2:
            data2=myfile2.readlines()
            newBigrams = [b for l in data2 for b in zip(l.split()[:-1], l.split()[1:])]
        for everyElement in newBigrams:
         if everyElement in bigrams.keys():
            bigrams[everyElement]+=1
         else:
            bigrams[everyElement]=1

    #unigrams - returns number of all words at all corpuses
    return wordsTotal
pass


# validate arguments length before continuing
if len(sys.argv) != 4:
    sys.exit('Invalid argument number!, please make sure you run the the command as follow: '
                 'python hw2.py <FolderWithInputFiles1>  <FolderWithInputFiles2>  <FolderForOutputFiles>')
# validate arguments length before continuing

if __name__ == "__main__":
    print(calculate_Unigrams(sys.argv))
    calculatePMI()
    for key, value in pmiResults.items():
        print(key,value)
