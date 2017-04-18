import sys,os,math,io, itertools
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
mutualTrigramsFromResults={}

def calculateMutualCollacationsTrigram():
    global TtestTrigramsAResults
    global TtestTrigramsBResults
    global X3TrigramsAResults
    global X3TrigramsBResults
    intersect= {}
    i=iter(TtestTrigramsAResults)
    TtestTrigramsAResults=dict((k) for k in TtestTrigramsAResults)
    TtestTrigramsAResults=sorted(TtestTrigramsAResults.items(), key=lambda x: (x[1]),reverse=True)[:10000]
    TtestTrigramsAResults=dict((k) for k in TtestTrigramsAResults)
    i=iter(TtestTrigramsBResults)
    TtestTrigramsBResults=dict((k) for k in TtestTrigramsBResults)
    TtestTrigramsBResults=sorted(TtestTrigramsBResults.items(), key=lambda x: (x[1]),reverse=True)[:10000]
    TtestTrigramsBResults=dict((k) for k in TtestTrigramsBResults)
    i=iter(X3TrigramsAResults)
    X3TrigramsAResults=dict((k) for k in X3TrigramsAResults)
    X3TrigramsAResults=sorted(X3TrigramsAResults.items(), key=lambda x: (x[1]),reverse=True)[:10000]
    X3TrigramsAResults=dict((k) for k in X3TrigramsAResults)
    i=iter(X3TrigramsBResults)
    X3TrigramsBResults=dict((k) for k in X3TrigramsBResults)
    X3TrigramsBResults=sorted(X3TrigramsBResults.items(), key=lambda x: (x[1]),reverse=True)[:10000]
    X3TrigramsBResults=dict((k) for k in X3TrigramsBResults)

    for key in TtestTrigramsAResults:
       if key in TtestTrigramsBResults:
           if key in X3TrigramsAResults:
               if key in X3TrigramsBResults:
                 intersect[key]=0
    print(intersect)


def saveTop100Results(fileName2Save, resultsToSave): # saving top 100 results from any dictionary that passed
 file = io.open(fileName2Save, 'w+', encoding='utf8')
 for key,value in sorted(resultsToSave.items(), key=lambda x: (-x[1], x[0]),reverse=True)[:100]:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateTtestTrigramsA(): # t3_a =  [ P(xyz)-P(x)P(y)P(z) ] / [sqrt(P(xyz)/N)]
 global TtestTrigramsAResults
 for everyTrigramElement in trigrams:
  if frequencyOfEachWord[everyTrigramElement[0]]>=20 and frequencyOfEachWord[everyTrigramElement[1]]>=20 and frequencyOfEachWord[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
     Pxyz=trigrams[everyTrigramElement]/trigramsTotal
     Px=frequencyOfEachWord[everyTrigramElement[0]]/wordsTotal
     Py=frequencyOfEachWord[everyTrigramElement[1]]/wordsTotal
     Pz=frequencyOfEachWord[everyTrigramElement[2]]/wordsTotal
     TtestTrigramsAResults[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Px*Py*Pz)/math.sqrt(Pxyz/wordsTotal)))
 file = io.open('ttest_tri_a.txt', 'w+', encoding='utf8')
 TtestTrigramsAResults=sorted(TtestTrigramsAResults.items(), key=lambda x: (x[1]),reverse=True)
 for key,value in TtestTrigramsAResults:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()
 #saveTop100Results('ttest_tri_a.txt',TtestTrigramsAResults) # saving top 100 results: ttest_tri_a.txt

def calculateTtestTrigramsB(): # t3_b = [ P(xyz)-P(xy)P(yz) ] / [sqrt(P(xyz)/N)]
  global TtestTrigramsBResults
  for everyTrigramElement in trigrams:
    if frequencyOfEachWord[everyTrigramElement[0]]>=20 and frequencyOfEachWord[everyTrigramElement[1]]>=20 and frequencyOfEachWord[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
       Pxyz=trigrams[everyTrigramElement]/trigramsTotal
       xy = everyTrigramElement[0:2]
       Pxy=bigrams[tuple(xy)]/bigramsTotal
       yz = everyTrigramElement[1:3]
       Pyz=bigrams[tuple(yz)]/bigramsTotal
       TtestTrigramsBResults[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Pxy*Pyz)/math.sqrt(Pxyz/wordsTotal)))
  file = io.open('ttest_tri_b.txt', 'w+', encoding='utf8')
  TtestTrigramsBResults=sorted(TtestTrigramsBResults.items(), key=lambda x: (x[1]),reverse=True)
  for key,value in TtestTrigramsBResults:
     file.write(str(key)+" "+str(value)+"\n")
  file.close()
  #saveTop100Results('ttest_tri_b.txt',TtestTrigramsBResults) # saving top 100 results: ttest_tri_b.txt

def calculateX3TestTrigramsA(): # x3_a = [ P(xyz)-P(x)P(y)P(z) ] / [P(x)P(y)P(z)]
 global X3TrigramsAResults
 for everyTrigramElement in trigrams:
  if frequencyOfEachWord[everyTrigramElement[0]]>=20 and frequencyOfEachWord[everyTrigramElement[1]]>=20 and frequencyOfEachWord[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
       Pxyz=trigrams[everyTrigramElement]/trigramsTotal
       Px=frequencyOfEachWord[everyTrigramElement[0]]/wordsTotal
       Py=frequencyOfEachWord[everyTrigramElement[1]]/wordsTotal
       Pz=frequencyOfEachWord[everyTrigramElement[2]]/wordsTotal
       X3TrigramsAResults[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Px*Py*Pz)/(Px*Py*Pz)))
 file = io.open('xtest_tri_a.txt', 'w+', encoding='utf8')
 X3TrigramsAResults=sorted(X3TrigramsAResults.items(), key=lambda x: (x[1]),reverse=True)
 for key,value in X3TrigramsAResults:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()
 #saveTop100Results('xtest_tri_a.txt',X3TrigramsAResults) # saving top 100 results: xtest_tri_a.txt

def calculateX3TestTrigramsB(): # x3_b =  [ P(xyz)-P(xy)P(yz) ] / [P(xy)P(yz)]
 global X3TrigramsBResults
 for everyTrigramElement in trigrams:
  if frequencyOfEachWord[everyTrigramElement[0]]>=20 and frequencyOfEachWord[everyTrigramElement[1]]>=20 and frequencyOfEachWord[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
   Pxyz=trigrams[everyTrigramElement]/trigramsTotal
   xy = everyTrigramElement[0:2]
   Pxy=bigrams[tuple(xy)]/bigramsTotal
   yz = everyTrigramElement[1:3]
   Pyz=bigrams[tuple(yz)]/bigramsTotal
   X3TrigramsBResults[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Pxy*Pyz)/ (Pxy*Pyz)))
 file = io.open('xtest_tri_b.txt', 'w+', encoding='utf8')
 X3TrigramsBResults=sorted(X3TrigramsBResults.items(), key=lambda x: (x[1]),reverse=True)
 for key,value in X3TrigramsBResults:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()
 #saveTop100Results('xtest_tri_b.txt',X3TrigramsBResults)  # saving top 100 results: xtest_tri_b.txt

def calculateX2TestBigrams(): #x = [ P(xy)-P(x)P(y) ] / [P(x)P(y)]
 global X2TestResults
 for everyElement in bigrams:
  if frequencyOfEachWord[everyElement[0]]>=20 and frequencyOfEachWord[everyElement[1]]>=20: #Px and Py should be greater than 20
   Pxy=bigrams[tuple(everyElement)]/bigramsTotal
   Px=frequencyOfEachWord[everyElement[0]]/wordsTotal
   Py=frequencyOfEachWord[everyElement[1]]/wordsTotal
   X2TestResults[everyElement]=float("{0:.3f}".format((Pxy-Px*Py)/(Px*Py)))
 file = io.open('xtest_pair.txt', 'w+', encoding='utf8')
 X2TestResults=sorted(X2TestResults.items(), key=lambda x: (x[1]),reverse=True)
 for key,value in X2TestResults:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()
 #saveTop100Results('xtest_pair.txt',X2TestResults)  # saving top 100 results:   xtest_pair.txt

def calculateTtestBigrams(): #t = [ P(xy)-P(x)P(y) ] / [sqrt(P(xy)/N)    N=wordsTotal
 global tTestResults
 for everyElement in bigrams:
   if frequencyOfEachWord[everyElement[0]]>=20 and frequencyOfEachWord[everyElement[1]]>=20: #Px and Py should be greater than 20
    Pxy=bigrams[tuple(everyElement)]/bigramsTotal
    Px=frequencyOfEachWord[everyElement[0]]/wordsTotal
    Py=frequencyOfEachWord[everyElement[1]]/wordsTotal
    tTestResults[everyElement]=float("{0:.3f}".format((Pxy-Px*Py)/ math.sqrt(Pxy/wordsTotal)))
 file = io.open('ttest_pair.txt', 'w+', encoding='utf8')
 tTestResults=sorted(tTestResults.items(), key=lambda x: (x[1]),reverse=True)
 for key,value in tTestResults:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()
 #saveTop100Results('ttest_pair.txt',tTestResults)  # saving top 100 results: ttest_pair.txt

def calculatePMIBigrams(): #PMI(x,y) = log(P(xy)/(P(x)*P(y))
 global pmiResults
 for everyElement in bigrams:
  if frequencyOfEachWord[everyElement[0]]>=20 and frequencyOfEachWord[everyElement[1]]>=20: #Px and Py should be greater than 20
   Pxy=bigrams[tuple(everyElement)]/bigramsTotal
   Px=frequencyOfEachWord[everyElement[0]]/wordsTotal
   Py=frequencyOfEachWord[everyElement[1]]/wordsTotal
   pmiResults[everyElement]=float("{0:.3f}".format(math.log(Pxy/(Px*Py),2)))
 file = io.open('pmi_pair.txt', 'w+', encoding='utf8')
 pmiResults=sorted(pmiResults.items(), key=lambda x: (x[1]),reverse=True)
 for key,value in pmiResults:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()
 #saveTop100Results('pmi_pair.txt',pmiResults) # saving top 100 results: pmi_pair.txt

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
    filesFirstCorpus = [f for f in listdir(sys.argv[1]) if isfile(os.path.join(sys.argv[1], f))]
    filesSecondCorpus = [f for f in listdir(sys.argv[2]) if isfile(os.path.join(sys.argv[2], f))]

    for name in filesFirstCorpus: #calculating Bigrams in  testset_literature start
        with open(sys.argv[1] + '\\' + name, encoding="utf8") as fileForWordsCount:
            words = [word for line in fileForWordsCount for word in line.split()]
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
        fileForWordsCount.close()

        #calculating Bigrams P(word1, word2) in 1st corpus: start
        with open (sys.argv[1] + '\\' + name, encoding="utf8") as bigramFile:
            data=bigramFile.readlines()
            newBigrams=[b for l in data for b in zip(l.split()[:-1], l.split()[1:])]
        #Bigram adding
        for everyElement in newBigrams:
         if tuple(everyElement) in bigrams.keys():
            bigrams[tuple(everyElement)]+=1
         else:
            bigrams[tuple(everyElement)]=1
            bigramsTotal+=1
         bigramFile.close()

    for name in filesSecondCorpus: #calculating Bigrams in  haaretz.heb start
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
         if tuple(everyElement) in bigrams.keys():
            bigrams[tuple(everyElement)]+=1
         else:
            bigrams[tuple(everyElement)]=1
            bigramsTotal+=1
    file = io.open('freq_raw.txt', 'w+', encoding='utf8')       # saving: freq_raw.txt
    for key,value in sorted(bigrams.items(), key=lambda x: (-x[1], x[0])):
      file.write(str(key)+" "+str(float("{0:.3f}".format((value/wordsTotal)*1000)))+"\n") #multiply by 1000
    file.close()
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
    calculateMutualCollacationsTrigram()
