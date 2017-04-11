import sys,os,math
from os import listdir
from os.path import isfile, join
from collections import Counter

bigrams={}  #all of bigrams will be there in that var
frequencyOfEachWord={}
pmiResults={}
tTestResults={}
X2TestResults={}
wordsTotal=0 # unigrams - counter for all words in corpuses

def calculateX2Test(): #x = [ P(xy)-P(x)P(y) ] / [P(x)P(y)]
 global X2TestResults
 for everyElement in bigrams:
   Pxy=bigrams[everyElement]
   Px=frequencyOfEachWord[everyElement[0]]
   Py=frequencyOfEachWord[everyElement[1]]
   x2Test=(Pxy-Px*Py)/Px*Py
   X2TestResults[everyElement]=x2Test

def calculateTtest(): #t = [ P(xy)-P(x)P(y) ] / [sqrt(P(xy)/N)    N=wordsTotal
 global tTestResults
 for everyElement in bigrams:
   Pxy=bigrams[everyElement]
   Px=frequencyOfEachWord[everyElement[0]]
   Py=frequencyOfEachWord[everyElement[1]]
   tTest=(Pxy-Px*Py)/math.sqrt(Pxy)/wordsTotal
   tTestResults[everyElement]=tTest

def calculatePMI(): #PMI(x,y) = log(P(xy)/P(x)*P(y) * 1000/N      N=wordsTotal
 global pmiResults
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

    for name in filesENG: #calculating Bigrams in  testset_literature start
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

        #calculating Bigrams P(word1, word2) in 1st corpus: start
        with open (sys.argv[1] + '\\' + name, encoding="utf8") as myfile:
            data=myfile.readlines()
            newBigrams=[b for l in data for b in zip(l.split()[:-1], l.split()[1:])]
        #Bigram adding
        for everyElement in newBigrams:
         if everyElement in bigrams.keys():
            bigrams[everyElement]+=1
         else:
            bigrams[everyElement]=1

    for name in filesHEB: #calculating Bigrams in  haaretz.heb start
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

        #calculating Bigrams P(word1, word2) in 2nd corpus: start
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
    #for key, value in pmiResults.items():
    #    print(key,value)
    calculateTtest()
    #for key, value in tTestResults.items():
    #    print(key,value)
    calculateX2Test()
    for key, value in X2TestResults.items():
        print(key,value)
