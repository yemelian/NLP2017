import sys,os,math,io
from os import listdir
from os.path import isfile

bigrams={}  #all of bigrams will be there in that var
trigrams={} #all of trigrams will be there in that var
frequencyOfEachWord={} #probabillity of single word at corpuses
pmiResults={}
tTestResults={}
X2TestResults={}
TtestTrigramsAResults={}
TtestTrigramsBResults={}
X3TrigramsAResults={}
X3TrigramsBResults={}
wordsTotal=0 # unigrams - counter for all words in corpuses
bigramsTotal=0 # bigrams - counter for all bigrams in corpuses
trigramsTotal=0 # trigrams - counter for all trigrams in corpuses

def saveTop100Results(fileName2Save, resultsToSave): # saving top 100 results from any dictionary that passed
 file = io.open(fileName2Save, 'w+', encoding='utf8')
 for key,value in sorted(resultsToSave.items(), key=lambda x: (-x[1], x[0]))[:100]:
     file.write(str(key)+" "+str(value))
 file.close()

def calculateTtestTrigramsA(): # t3_a =  [ P(xyz)-P(x)P(y)P(z) ] / [sqrt(P(xyz)/N)]
 global TtestTrigramsAResults
 for everyElement in trigrams:
   Pxyz=trigrams[everyElement]/trigramsTotal
   Px=frequencyOfEachWord[everyElement[0]]/wordsTotal
   Py=frequencyOfEachWord[everyElement[1]]/wordsTotal
   Pz=frequencyOfEachWord[everyElement[2]]/wordsTotal
   tTestA=(Pxyz-Px*Py*Pz)/math.sqrt(Pxyz/wordsTotal)
   TtestTrigramsAResults[everyElement]=tTestA
 saveTop100Results('ttest_tri_a.txt',TtestTrigramsAResults) # saving top 100 results: ttest_tri_a.txt

def calculateTtestTrigramsB(): # t3_b = [ P(xyz)-P(xy)P(yz) ] / [sqrt(P(xyz)/N)]
  global TtestTrigramsBResults
  for everyTrigramElement in trigrams:
    if frequencyOfEachWord[everyTrigramElement[0]]>=20 and frequencyOfEachWord[everyTrigramElement[1]]>=20 and frequencyOfEachWord[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
       Pxyz=trigrams[everyTrigramElement]/trigramsTotal
       xy = everyTrigramElement[0:2]
       Pxy=bigrams[tuple(xy)]/bigramsTotal
       yz = everyTrigramElement[1:3]
       Pyz=bigrams[tuple(yz)]/bigramsTotal
       tTestB=(Pxyz-Pxy*Pyz)/math.sqrt(Pxyz/wordsTotal)
       TtestTrigramsBResults[everyTrigramElement]=tTestB
  saveTop100Results('ttest_tri_b.txt',TtestTrigramsBResults) # saving top 100 results: ttest_tri_b.txt

def calculateX3TestTrigramsA(): # x3_a = [ P(xyz)-P(x)P(y)P(z) ] / [P(x)P(y)P(z)]
 global X3TrigramsAResults
 for everyTrigramElement in trigrams:
  if frequencyOfEachWord[everyTrigramElement[0]]>=20 and frequencyOfEachWord[everyTrigramElement[1]]>=20 and frequencyOfEachWord[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
       Pxyz=trigrams[everyTrigramElement]/trigramsTotal
       Px=frequencyOfEachWord[everyTrigramElement[0]]/wordsTotal
       Py=frequencyOfEachWord[everyTrigramElement[1]]/wordsTotal
       Pz=frequencyOfEachWord[everyTrigramElement[2]]/wordsTotal
       X3A=(Pxyz-Px*Py*Pz)/ (Px*Py*Pz)
       X3TrigramsAResults[everyTrigramElement]=X3A
 saveTop100Results('xtest_tri_a.txt',X3TrigramsAResults) # saving top 100 results: xtest_tri_a.txt

def calculateX3TestTrigramsB(): # x3_b =  [ P(xyz)-P(xy)P(yz) ] / [P(xy)P(yz)]
 global X3TrigramsBResults
 for everyTrigramElement in trigrams:
  if frequencyOfEachWord[everyTrigramElement[0]]>=20 and frequencyOfEachWord[everyTrigramElement[1]]>=20 and frequencyOfEachWord[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
   Pxyz=trigrams[everyTrigramElement]/trigramsTotal
   xy = everyTrigramElement[0:2]
   Pxy=bigrams[tuple(xy)]/bigramsTotal
   yz = everyTrigramElement[1:3]
   Pyz=bigrams[tuple(yz)]/bigramsTotal
   X3B=(Pxyz-Pxy*Pyz)/ (Pxy*Pyz)
   X3TrigramsBResults[everyTrigramElement]=X3B
 saveTop100Results('xtest_tri_b.txt',X3TrigramsBResults)  # saving top 100 results: xtest_tri_b.txt

def calculateX2TestBigrams(): #x = [ P(xy)-P(x)P(y) ] / [P(x)P(y)] N=wordsTotal
 global X2TestResults
 for everyElement in bigrams:
  if frequencyOfEachWord[everyElement[0]]>=20 and frequencyOfEachWord[everyElement[1]]>=20: #Px and Py should be greater than 20
   Pxy=bigrams[everyElement]/bigramsTotal
   Px=frequencyOfEachWord[everyElement[0]]/wordsTotal
   Py=frequencyOfEachWord[everyElement[1]]/wordsTotal
   x2Test=(Pxy-Px*Py)/Px*Py
   X2TestResults[everyElement]=x2Test
 saveTop100Results('xtest_pair.txt',X2TestResults)  # saving top 100 results:   xtest_pair.txt

def calculateTtestBigrams(): #t = [ P(xy)-P(x)P(y) ] / [sqrt(P(xy)/N)    N=wordsTotal
 global tTestResults
 for everyElement in bigrams:
   if frequencyOfEachWord[everyElement[0]]>=20 and frequencyOfEachWord[everyElement[1]]>=20: #Px and Py should be greater than 20
    Pxy=bigrams[everyElement]/bigramsTotal
    Px=frequencyOfEachWord[everyElement[0]]/wordsTotal
    Py=frequencyOfEachWord[everyElement[1]]/wordsTotal
    tTest=(Pxy-Px*Py)/math.sqrt(Pxy)/wordsTotal
    tTestResults[everyElement]=tTest
 saveTop100Results('ttest_pair.txt',tTestResults)  # saving top 100 results: ttest_pair.txt

def calculatePMIBigrams(): #PMI(x,y) = log(P(xy)/P(x)*P(y)
 global pmiResults
 for everyElement in bigrams:
  if frequencyOfEachWord[everyElement[0]]>=20 and frequencyOfEachWord[everyElement[1]]>=20: #Px and Py should be greater than 20
   Pxy=bigrams[everyElement]/bigramsTotal
   Px=frequencyOfEachWord[everyElement[0]]/wordsTotal
   Py=frequencyOfEachWord[everyElement[1]]/wordsTotal
   PMI=math.log((Pxy/Px*Py),2)
   pmiResults[everyElement]=PMI
 saveTop100Results('pmi_pair.txt',pmiResults) # saving top 100 results: pmi_pair.txt

def calculateTrigrams(argv):
    global trigrams
    global trigramsTotal
    # Define paths to corpuses: sys.argv[1] = r'C:\Temp\NLP\testset_literature' sys.argv[2] = r'C:\Temp\NLP\haaretz.heb'
    filesENG = [f for f in listdir(sys.argv[1]) if isfile(os.path.join(sys.argv[1], f))]
    filesHEB = [f for f in listdir(sys.argv[2]) if isfile(os.path.join(sys.argv[2], f))]

    for name in filesENG: #calculating Bigrams in  testset_literature start
        #calculating Trigrams P(word1, word2, word3) in 1st corpus: start
        with open (sys.argv[1] + '\\' + name, encoding="utf8") as myfile:
            data=myfile.readlines()
            N=3
            newTrigrams = [b for l in data for b in zip(l.split()[:-1],l.split()[1:], l.split()[2:])]
          #Trigram adding
        for everyElement in newTrigrams:
             if everyElement in trigrams.keys():
                trigrams[everyElement]+=1
             else:
                trigrams[everyElement]=1
                trigramsTotal+=1

    for name in filesHEB: #calculating Bigrams in  testset_literature start
        #calculating Trigrams P(word1, word2, word3) in 1st corpus: start
        with open (sys.argv[2] + '\\' + name, encoding="utf8") as myfile:
            data=myfile.readlines()
            N=3
            newTrigrams = [b for l in data for b in zip(l.split()[:-1],l.split()[1:], l.split()[2:])]
          #Trigram adding
        for everyElement in newTrigrams:
             if everyElement in trigrams.keys():
                trigrams[everyElement]+=1
             else:
                trigrams[everyElement]=1
                trigramsTotal+=1

def calculate_Unigrams(argv):
    global bigrams
    global frequencyOfEachWord
    global wordsTotal
    global bigramsTotal
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
            bigramsTotal+=1

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
            bigramsTotal+=1
    # saving: freq_raw.txt
    file = io.open('freq_raw.txt', 'w+', encoding='utf8')
    for key,value in bigrams.items():
     file.write(str(key)+" "+str((value/wordsTotal)*1000)) #multiply by 1000
    file.close()
    #unigrams - returns number of all words at all corpuses
    return wordsTotal
pass

if len(sys.argv) != 4: # validate arguments length before continuing ##############################################
    sys.exit('Invalid argument number!, please make sure you run the the command as follow: '
                 'python hw2.py <FolderWithInputFiles1>  <FolderWithInputFiles2>  <FolderForOutputFiles>')
# validate arguments length before continuing #####################################################################

if __name__ == "__main__":
    calculate_Unigrams(sys.argv)
    calculatePMIBigrams()
    calculateTtestBigrams()
    calculateX2TestBigrams()
    calculateTrigrams(sys.argv)
    calculateTtestTrigramsA()
    calculateTtestTrigramsB()
    calculateX3TestTrigramsA()
    calculateX3TestTrigramsB()
