import sys,os,math,io, itertools
from os import listdir
from os.path import isfile

bigrams={}  #all of bigrams will be there in that var
bigramsCorpus1={}  #all of Corpus1 bigrams will be there in that var
bigramsCorpus2={}  #all of Corpus1 bigrams will be there in that var
trigrams={} #all of trigrams will be there in that var
trigramsCorpus1={} #all of Corpus1 trigrams will be there in that var
trigramsCorpus2={} #all of Corpus2 trigrams will be there in that var
frequencyOfEachWord={} #probabillity of single word at corpuses
frequencyOfEachWordCorpus1={} #probabillity of Corpus1 single word at corpus1
frequencyOfEachWordCorpus2={} #probabillity of Corpus1 single word at corpus2
pmiResults={} #pmi results of Corpuses
pmiCorpus1Results={} #pmi results of Corpue1
pmiCorpus2Results={} #pmi results of Corpus2
tTestResults={} #tTest results of Corpuses
tTestCorpus1Results={} #tTest results of Corpus1
tTestCorpus2Results={} #tTest results of Corpus2
X2TestResults={} #X2Test results of Corpuses
X2TestCorpus1Results={} #X2Test results of Corpus1
X2TestCorpus2Results={} #X2Test results of Corpus2
TtestTrigramsAResults={} #TtestA results for trigrams of Corpuses
TtestTrigramsACorpus1Results={} #TtestA results for trigrams of Corpus1
TtestTrigramsACorpus2Results={} #TtestA results for trigrams of Corpus2
TtestTrigramsBResults={} #TtestB results for trigrams of Corpuses
TtestTrigramsBCorpus1Results={} #TtestB results for trigrams of Corpus1
TtestTrigramsBCorpus2Results={} #TtestB results for trigrams of Corpus2
X3TrigramsAResults={} #X3A results for trigrams of Corpuses
X3TrigramsACorpus1Results={} #X3A results for trigrams of Corpus1
X3TrigramsACorpus2Results={} #X3A results for trigrams of Corpus2
X3TrigramsBResults={} #X3B results for trigrams of Corpuses
X3TrigramsBCorpus1Results={} #X3B results for trigrams of Corpus1
X3TrigramsBCorpus2Results={} #X3B results for trigrams of Corpus2
wordsTotal=0 # unigrams - counter for all words in corpuses
wordsTotalCorpus1=0 # unigrams - counter for all words in corpus1
wordsTotalCorpus2=0 # unigrams - counter for all words in corpus2
bigramsTotal=0 # bigrams - counter for all bigrams in corpuses
bigramsTotalCorpus1=0  # bigrams - counter for all bigrams in corpus1
bigramsTotalCorpus2=0  # bigrams - counter for all bigrams in corpus2
trigramsTotal=0 # trigrams - counter for all trigrams in corpuses
trigramsTotalCorpus1=0 # trigrams - counter for all trigrams in corpus1
trigramsTotalCorpus2=0 # trigrams - counter for all trigrams in corpus2
mutualTrigramsFromResults={}

def calculateMutualCollacationsTrigram():
    global TtestTrigramsAResults
    global TtestTrigramsBResults
    global X3TrigramsAResults
    global X3TrigramsBResults
    intersect= {}
    i=iter(TtestTrigramsAResults)
    TtestTrigramsAResults=dict((k) for k in TtestTrigramsAResults)
    TtestTrigramsAResults=sorted(TtestTrigramsAResults.items(), key=lambda x: (x[1]),reverse=True)
    TtestTrigramsAResults=dict((k) for k in TtestTrigramsAResults)
    i=iter(TtestTrigramsBResults)
    TtestTrigramsBResults=dict((k) for k in TtestTrigramsBResults)
    TtestTrigramsBResults=sorted(TtestTrigramsBResults.items(), key=lambda x: (x[1]),reverse=True)
    TtestTrigramsBResults=dict((k) for k in TtestTrigramsBResults)
    i=iter(X3TrigramsAResults)
    X3TrigramsAResults=dict((k) for k in X3TrigramsAResults)
    X3TrigramsAResults=sorted(X3TrigramsAResults.items(), key=lambda x: (x[1]),reverse=True)
    X3TrigramsAResults=dict((k) for k in X3TrigramsAResults)
    i=iter(X3TrigramsBResults)
    X3TrigramsBResults=dict((k) for k in X3TrigramsBResults)
    X3TrigramsBResults=sorted(X3TrigramsBResults.items(), key=lambda x: (x[1]),reverse=True)
    X3TrigramsBResults=dict((k) for k in X3TrigramsBResults)

    for key in TtestTrigramsAResults:
       if key in TtestTrigramsBResults:
           if key in X3TrigramsAResults:
               if key in X3TrigramsBResults:
                 intersect[key]=0

def calculateTtestTrigramsA(): # t3_a =  [ P(xyz)-P(x)P(y)P(z) ] / [sqrt(P(xyz)/N)] ALL CORPUSES
 global TtestTrigramsAResults
 for everyTrigramElement in trigrams:
  if frequencyOfEachWord[everyTrigramElement[0]]>=20 and frequencyOfEachWord[everyTrigramElement[1]]>=20 and frequencyOfEachWord[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
     Pxyz=trigrams[everyTrigramElement]/trigramsTotal
     Px=frequencyOfEachWord[everyTrigramElement[0]]/wordsTotal
     Py=frequencyOfEachWord[everyTrigramElement[1]]/wordsTotal
     Pz=frequencyOfEachWord[everyTrigramElement[2]]/wordsTotal
     TtestTrigramsAResults[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Px*Py*Pz)/math.sqrt(Pxyz/wordsTotal)))
 file = io.open('ttest_tri_a.txt', 'w+', encoding='utf8')
 TtestTrigramsAResults=sorted(TtestTrigramsAResults.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in TtestTrigramsAResults:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateTtestTrigramsACorpus1(): # t3_a =  [ P(xyz)-P(x)P(y)P(z) ] / [sqrt(P(xyz)/N)] CORPUS1
 global TtestTrigramsACorpus1Results
 for everyTrigramElement in trigramsCorpus1:
  if frequencyOfEachWordCorpus1[everyTrigramElement[0]]>=20 and frequencyOfEachWordCorpus1[everyTrigramElement[1]]>=20 and frequencyOfEachWordCorpus1[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
     Pxyz=trigramsCorpus1[everyTrigramElement]/trigramsTotalCorpus1
     Px=frequencyOfEachWordCorpus1[everyTrigramElement[0]]/wordsTotalCorpus1
     Py=frequencyOfEachWordCorpus1[everyTrigramElement[1]]/wordsTotalCorpus1
     Pz=frequencyOfEachWordCorpus1[everyTrigramElement[2]]/wordsTotalCorpus1
     TtestTrigramsACorpus1Results[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Px*Py*Pz)/math.sqrt(Pxyz/wordsTotalCorpus1)))
 file = io.open('ttest_tri_a_corpus1.txt', 'w+', encoding='utf8')
 TtestTrigramsACorpus1Results=sorted(TtestTrigramsACorpus1Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in TtestTrigramsACorpus1Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateTtestTrigramsACorpus2(): # t3_a =  [ P(xyz)-P(x)P(y)P(z) ] / [sqrt(P(xyz)/N)] CORPUS2
 global TtestTrigramsACorpus2Results
 for everyTrigramElement in trigramsCorpus2:
  if frequencyOfEachWordCorpus2[everyTrigramElement[0]]>=20 and frequencyOfEachWordCorpus2[everyTrigramElement[1]]>=20 and frequencyOfEachWordCorpus2[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
     Pxyz=trigramsCorpus2[everyTrigramElement]/trigramsTotalCorpus2
     Px=frequencyOfEachWordCorpus2[everyTrigramElement[0]]/wordsTotalCorpus2
     Py=frequencyOfEachWordCorpus2[everyTrigramElement[1]]/wordsTotalCorpus2
     Pz=frequencyOfEachWordCorpus2[everyTrigramElement[2]]/wordsTotalCorpus2
     TtestTrigramsACorpus2Results[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Px*Py*Pz)/math.sqrt(Pxyz/wordsTotalCorpus2)))
 file = io.open('ttest_tri_a_corpus2.txt', 'w+', encoding='utf8')
 TtestTrigramsACorpus2Results=sorted(TtestTrigramsACorpus2Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in TtestTrigramsACorpus2Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

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

def calculateTtestTrigramsBCorpus1(): # t3_b = [ P(xyz)-P(xy)P(yz) ] / [sqrt(P(xyz)/N)] CORPUS1
  global TtestTrigramsBCorpus1Results
  for everyTrigramElement in trigramsCorpus1:
    if frequencyOfEachWordCorpus1[everyTrigramElement[0]]>=20 and frequencyOfEachWordCorpus1[everyTrigramElement[1]]>=20 and frequencyOfEachWordCorpus1[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
       Pxyz=trigramsCorpus1[everyTrigramElement]/trigramsTotalCorpus1
       xy = everyTrigramElement[0:2]
       Pxy=bigramsCorpus1[tuple(xy)]/bigramsTotalCorpus1
       yz = everyTrigramElement[1:3]
       Pyz=bigramsCorpus1[tuple(yz)]/bigramsTotalCorpus1
       TtestTrigramsBCorpus1Results[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Pxy*Pyz)/math.sqrt(Pxyz/wordsTotalCorpus1)))
  file = io.open('ttest_tri_b_corpus1.txt', 'w+', encoding='utf8')
  TtestTrigramsBCorpus1Results=sorted(TtestTrigramsBCorpus1Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
  for key,value in TtestTrigramsBCorpus1Results:
     file.write(str(key)+" "+str(value)+"\n")
  file.close()

def calculateTtestTrigramsBCorpus2(): # t3_b = [ P(xyz)-P(xy)P(yz) ] / [sqrt(P(xyz)/N)] CORPUS2
  global TtestTrigramsBCorpus2Results
  for everyTrigramElement in trigramsCorpus2:
    if frequencyOfEachWordCorpus2[everyTrigramElement[0]]>=20 and frequencyOfEachWordCorpus2[everyTrigramElement[1]]>=20 and frequencyOfEachWordCorpus2[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
       Pxyz=trigramsCorpus2[everyTrigramElement]/trigramsTotalCorpus2
       xy = everyTrigramElement[0:2]
       Pxy=bigramsCorpus2[tuple(xy)]/bigramsTotalCorpus2
       yz = everyTrigramElement[1:3]
       Pyz=bigramsCorpus2[tuple(yz)]/bigramsTotalCorpus2
       TtestTrigramsBCorpus2Results[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Pxy*Pyz)/math.sqrt(Pxyz/wordsTotalCorpus2)))
  file = io.open('ttest_tri_b_corpus2.txt', 'w+', encoding='utf8')
  TtestTrigramsBCorpus2Results=sorted(TtestTrigramsBCorpus2Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
  for key,value in TtestTrigramsBCorpus2Results:
     file.write(str(key)+" "+str(value)+"\n")
  file.close()

def calculateX3TestTrigramsA(): # x3_a = [ P(xyz)-P(x)P(y)P(z) ] / [P(x)P(y)P(z)] CORPUSES
 global X3TrigramsAResults
 for everyTrigramElement in trigrams:
  if frequencyOfEachWord[everyTrigramElement[0]]>=20 and frequencyOfEachWord[everyTrigramElement[1]]>=20 and frequencyOfEachWord[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
       Pxyz=trigrams[everyTrigramElement]/trigramsTotal
       Px=frequencyOfEachWord[everyTrigramElement[0]]/wordsTotal
       Py=frequencyOfEachWord[everyTrigramElement[1]]/wordsTotal
       Pz=frequencyOfEachWord[everyTrigramElement[2]]/wordsTotal
       X3TrigramsAResults[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Px*Py*Pz)/(Px*Py*Pz)))
 file = io.open('xtest_tri_a.txt', 'w+', encoding='utf8')
 X3TrigramsAResults=sorted(X3TrigramsAResults.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in X3TrigramsAResults:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateX3TestTrigramsACorpus1(): # x3_a = [ P(xyz)-P(x)P(y)P(z) ] / [P(x)P(y)P(z)] CORPUS1
 global X3TrigramsACorpus1Results
 for everyTrigramElement in trigramsCorpus1:
  if frequencyOfEachWordCorpus1[everyTrigramElement[0]]>=20 and frequencyOfEachWordCorpus1[everyTrigramElement[1]]>=20 and frequencyOfEachWordCorpus1[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
       Pxyz=trigramsCorpus1[everyTrigramElement]/trigramsTotalCorpus1
       Px=frequencyOfEachWordCorpus1[everyTrigramElement[0]]/wordsTotalCorpus1
       Py=frequencyOfEachWordCorpus1[everyTrigramElement[1]]/wordsTotalCorpus1
       Pz=frequencyOfEachWordCorpus1[everyTrigramElement[2]]/wordsTotalCorpus1
       X3TrigramsACorpus1Results[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Px*Py*Pz)/(Px*Py*Pz)))
 file = io.open('xtest_tri_a_corpus1.txt', 'w+', encoding='utf8')
 X3TrigramsACorpus1Results=sorted(X3TrigramsACorpus1Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in X3TrigramsACorpus1Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateX3TestTrigramsACorpus2(): # x3_a = [ P(xyz)-P(x)P(y)P(z) ] / [P(x)P(y)P(z)] CORPUS2
 global X3TrigramsACorpus2Results
 for everyTrigramElement in trigramsCorpus2:
  if frequencyOfEachWordCorpus2[everyTrigramElement[0]]>=20 and frequencyOfEachWordCorpus2[everyTrigramElement[1]]>=20 and frequencyOfEachWordCorpus2[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
       Pxyz=trigramsCorpus2[everyTrigramElement]/trigramsTotalCorpus2
       Px=frequencyOfEachWordCorpus2[everyTrigramElement[0]]/wordsTotalCorpus2
       Py=frequencyOfEachWordCorpus2[everyTrigramElement[1]]/wordsTotalCorpus2
       Pz=frequencyOfEachWordCorpus2[everyTrigramElement[2]]/wordsTotalCorpus2
       X3TrigramsACorpus2Results[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Px*Py*Pz)/(Px*Py*Pz)))
 file = io.open('xtest_tri_a_corpus2.txt', 'w+', encoding='utf8')
 X3TrigramsACorpus2Results=sorted(X3TrigramsACorpus2Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in X3TrigramsACorpus2Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateX3TestTrigramsB(): # x3_b =  [ P(xyz)-P(xy)P(yz) ] / [P(xy)P(yz)] CORPUSES
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
 X3TrigramsBResults=sorted(X3TrigramsBResults.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in X3TrigramsBResults:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateX3TestTrigramsBCorpus1(): # x3_b =  [ P(xyz)-P(xy)P(yz) ] / [P(xy)P(yz)] CORPUS1
 global X3TrigramsBCorpus1Results
 for everyTrigramElement in trigramsCorpus1:
  if frequencyOfEachWordCorpus1[everyTrigramElement[0]]>=20 and frequencyOfEachWordCorpus1[everyTrigramElement[1]]>=20 and frequencyOfEachWordCorpus1[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
   Pxyz=trigramsCorpus1[everyTrigramElement]/trigramsTotalCorpus1
   xy = everyTrigramElement[0:2]
   Pxy=bigramsCorpus1[tuple(xy)]/bigramsTotalCorpus1
   yz = everyTrigramElement[1:3]
   Pyz=bigramsCorpus1[tuple(yz)]/bigramsTotalCorpus1
   X3TrigramsBCorpus1Results[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Pxy*Pyz)/ (Pxy*Pyz)))
 file = io.open('xtest_tri_b_corpus1.txt', 'w+', encoding='utf8')
 X3TrigramsBCorpus1Results=sorted(X3TrigramsBCorpus1Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in X3TrigramsBCorpus1Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateX3TestTrigramsBCorpus2(): # x3_b =  [ P(xyz)-P(xy)P(yz) ] / [P(xy)P(yz)] CORPUS2
 global X3TrigramsBCorpus2Results
 for everyTrigramElement in trigramsCorpus2:
  if frequencyOfEachWordCorpus2[everyTrigramElement[0]]>=20 and frequencyOfEachWordCorpus2[everyTrigramElement[1]]>=20 and frequencyOfEachWordCorpus2[everyTrigramElement[2]]>=20: #Px,Py,Pz should be greater than 20
   Pxyz=trigramsCorpus2[everyTrigramElement]/trigramsTotalCorpus2
   xy = everyTrigramElement[0:2]
   Pxy=bigramsCorpus2[tuple(xy)]/bigramsTotalCorpus2
   yz = everyTrigramElement[1:3]
   Pyz=bigramsCorpus2[tuple(yz)]/bigramsTotalCorpus2
   X3TrigramsBCorpus2Results[everyTrigramElement]=float("{0:.3f}".format((Pxyz-Pxy*Pyz)/ (Pxy*Pyz)))
 file = io.open('xtest_tri_b_corpus2.txt', 'w+', encoding='utf8')
 X3TrigramsBCorpus2Results=sorted(X3TrigramsBCorpus2Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in X3TrigramsBCorpus2Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateX2TestBigrams(): #x = [ P(xy)-P(x)P(y) ] / [P(x)P(y)] CORPUSES
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

def calculateX2TestBigramsCorpus1(): #x = [ P(xy)-P(x)P(y) ] / [P(x)P(y)] CORPUS1
 global X2TestCorpus1Results
 for everyElement in bigramsCorpus1:
  if frequencyOfEachWordCorpus1[everyElement[0]]>=20 and frequencyOfEachWordCorpus1[everyElement[1]]>=20: #Px and Py should be greater than 20
   Pxy=bigramsCorpus1[tuple(everyElement)]/bigramsTotalCorpus1
   Px=frequencyOfEachWordCorpus1[everyElement[0]]/wordsTotalCorpus1
   Py=frequencyOfEachWordCorpus1[everyElement[1]]/wordsTotalCorpus1
   X2TestCorpus1Results[everyElement]=float("{0:.3f}".format((Pxy-Px*Py)/(Px*Py)))
 file = io.open('xtest_pair_corpus1.txt', 'w+', encoding='utf8')
 X2TestCorpus1Results=sorted(X2TestCorpus1Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in X2TestCorpus1Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateX2TestBigramsCorpus2(): #x = [ P(xy)-P(x)P(y) ] / [P(x)P(y)] CORPUS2
 global X2TestCorpus2Results
 for everyElement in bigramsCorpus2:
  if frequencyOfEachWordCorpus2[everyElement[0]]>=20 and frequencyOfEachWordCorpus2[everyElement[1]]>=20: #Px and Py should be greater than 20
   Pxy=bigramsCorpus2[tuple(everyElement)]/bigramsTotalCorpus2
   Px=frequencyOfEachWordCorpus2[everyElement[0]]/wordsTotalCorpus2
   Py=frequencyOfEachWordCorpus2[everyElement[1]]/wordsTotalCorpus2
   X2TestCorpus2Results[everyElement]=float("{0:.3f}".format((Pxy-Px*Py)/(Px*Py)))
 file = io.open('xtest_pair_corpus2.txt', 'w+', encoding='utf8')
 X2TestCorpus2Results=sorted(X2TestCorpus2Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in X2TestCorpus2Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateTtestBigrams(): #t = [ P(xy)-P(x)P(y) ] / [sqrt(P(xy)/N)    N=wordsTotal  CORPUSES
 global tTestResults
 for everyElement in bigrams:
   if frequencyOfEachWord[everyElement[0]]>=20 and frequencyOfEachWord[everyElement[1]]>=20: #Px and Py should be greater than 20
    Pxy=bigrams[tuple(everyElement)]/bigramsTotal
    Px=frequencyOfEachWord[everyElement[0]]/wordsTotal
    Py=frequencyOfEachWord[everyElement[1]]/wordsTotal
    tTestResults[everyElement]=float("{0:.3f}".format((Pxy-Px*Py)/ math.sqrt(Pxy/wordsTotal)))
 file = io.open('ttest_pair.txt', 'w+', encoding='utf8')  # saving: ttest_pair.txt
 tTestResults=sorted(tTestResults.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in tTestResults:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateTtestBigramsCorpus1(): #t = [ P(xy)-P(x)P(y) ] / [sqrt(P(xy)/N)    N=wordsTotal  CORPUS1
 global tTestCorpus1Results
 for everyElement in bigramsCorpus1:
   if frequencyOfEachWordCorpus1[everyElement[0]]>=20 and frequencyOfEachWordCorpus1[everyElement[1]]>=20: #Px and Py should be greater than 20
    Pxy=bigramsCorpus1[tuple(everyElement)]/bigramsTotalCorpus1
    Px=frequencyOfEachWordCorpus1[everyElement[0]]/wordsTotalCorpus1
    Py=frequencyOfEachWordCorpus1[everyElement[1]]/wordsTotalCorpus1
    tTestCorpus1Results[everyElement]=float("{0:.3f}".format((Pxy-Px*Py)/ math.sqrt(Pxy/wordsTotalCorpus1)))
 file = io.open('ttest_pair_corpus1.txt', 'w+', encoding='utf8')  # saving: ttest_pair_corpus1.txt
 tTestCorpus1Results=sorted(tTestCorpus1Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in tTestCorpus1Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateTtestBigramsCorpus2(): #t = [ P(xy)-P(x)P(y) ] / [sqrt(P(xy)/N)    N=wordsTotal  CORPUS2
 global tTestCorpus2Results
 for everyElement in bigramsCorpus2:
   if frequencyOfEachWordCorpus2[everyElement[0]]>=20 and frequencyOfEachWordCorpus2[everyElement[1]]>=20: #Px and Py should be greater than 20
    Pxy=bigramsCorpus2[tuple(everyElement)]/bigramsTotalCorpus2
    Px=frequencyOfEachWordCorpus2[everyElement[0]]/wordsTotalCorpus2
    Py=frequencyOfEachWordCorpus2[everyElement[1]]/wordsTotalCorpus2
    tTestCorpus2Results[everyElement]=float("{0:.3f}".format((Pxy-Px*Py)/ math.sqrt(Pxy/wordsTotalCorpus2)))
 file = io.open('ttest_pair_corpus2.txt', 'w+', encoding='utf8')  # saving: ttest_pair_corpus2.txt
 tTestCorpus2Results=sorted(tTestCorpus2Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in tTestCorpus2Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculatePMIBigrams(): #PMI(x,y) = log(P(xy)/(P(x)*P(y)) CORPUSES
 global pmiResults
 for everyElement in bigrams:
  if frequencyOfEachWord[everyElement[0]]>=20 and frequencyOfEachWord[everyElement[1]]>=20: #Px and Py should be greater than 20
   Pxy=bigrams[tuple(everyElement)]/bigramsTotal
   Px=frequencyOfEachWord[everyElement[0]]/wordsTotal
   Py=frequencyOfEachWord[everyElement[1]]/wordsTotal
   pmiResults[everyElement]=float("{0:.3f}".format(math.log(Pxy/(Px*Py),2)))
 file = io.open('pmi_pair.txt', 'w+', encoding='utf8') # saving top 100 results: pmi_pair.txt
 pmiResults=sorted(pmiResults.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in pmiResults:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculatePMIBigramsCorpus1(): #PMI(x,y) = log(P(xy)/(P(x)*P(y)) CORPUS1
 global pmiCorpus1Results
 for everyElement in bigramsCorpus1:
  if frequencyOfEachWordCorpus1[everyElement[0]]>=20 and frequencyOfEachWordCorpus1[everyElement[1]]>=20: #Px and Py should be greater than 20
   Pxy=bigramsCorpus1[tuple(everyElement)]/bigramsTotalCorpus1
   Px=frequencyOfEachWordCorpus1[everyElement[0]]/wordsTotalCorpus1
   Py=frequencyOfEachWordCorpus1[everyElement[1]]/wordsTotalCorpus1
   pmiCorpus1Results[everyElement]=float("{0:.3f}".format(math.log(Pxy/(Px*Py),2)))
 file = io.open('pmi_pair_corpus1.txt', 'w+', encoding='utf8') # saving top 100 results: pmi_pair_corpus1.txt
 pmiCorpus1Results=sorted(pmiCorpus1Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in pmiCorpus1Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculatePMIBigramsCorpus2(): #PMI(x,y) = log(P(xy)/(P(x)*P(y)) CORPUS2
 global pmiCorpus2Results
 for everyElement in bigramsCorpus2:
  if frequencyOfEachWordCorpus2[everyElement[0]]>=20 and frequencyOfEachWordCorpus2[everyElement[1]]>=20: #Px and Py should be greater than 20
   Pxy=bigramsCorpus2[tuple(everyElement)]/bigramsTotalCorpus2
   Px=frequencyOfEachWordCorpus2[everyElement[0]]/wordsTotalCorpus2
   Py=frequencyOfEachWordCorpus2[everyElement[1]]/wordsTotalCorpus2
   pmiCorpus2Results[everyElement]=float("{0:.3f}".format(math.log(Pxy/(Px*Py),2)))
 file = io.open('pmi_pair_corpus2.txt', 'w+', encoding='utf8') # saving top 100 results: pmi_pair_corpus2.txt
 pmiCorpus2Results=sorted(pmiCorpus2Results.items(), key=lambda x: (x[1]),reverse=True)[:100]
 for key,value in pmiCorpus2Results:
     file.write(str(key)+" "+str(value)+"\n")
 file.close()

def calculateTrigrams(argv):
    global trigrams
    global trigramsCorpus1
    global trigramsCorpus2
    global trigramsTotal
    global trigramsTotalCorpus1
    global trigramsTotalCorpus2
    # Define paths to corpuses: sys.argv[1] = r'C:\Temp\NLP\testset_literature' sys.argv[2] = r'C:\Temp\NLP\haaretz.heb'
    filesFirstCorpus = [f for f in listdir(sys.argv[1]) if isfile(os.path.join(sys.argv[1], f))]
    filesSecondCorpus = [f for f in listdir(sys.argv[2]) if isfile(os.path.join(sys.argv[2], f))]

    for name in filesFirstCorpus: #calculating Bigrams in  testset_literature start
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

             if everyElement in trigramsCorpus1.keys():
                trigramsCorpus1[everyElement]+=1
             else:
                trigramsCorpus1[everyElement]=1
                trigramsTotalCorpus1+=1

    for name in filesSecondCorpus: #calculating Bigrams in  testset_literature start
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

             if everyElement in trigramsCorpus2.keys():
                trigramsCorpus2[everyElement]+=1
             else:
                trigramsCorpus2[everyElement]=1
                trigramsTotalCorpus2+=1

def calculate_Unigrams(argv):
    global bigrams
    global bigramsCorpus1
    global bigramsCorpus2
    global frequencyOfEachWord
    global frequencyOfEachWordCorpus1
    global frequencyOfEachWordCorpus2
    global wordsTotal
    global wordsTotalCorpus1
    global wordsTotalCorpus2
    global bigramsTotal
    global bigramsTotalCorpus1
    global bigramsTotalCorpus2
    # Define paths to corpuses: sys.argv[1] = r'C:\Temp\NLP\testset_literature' sys.argv[2] = r'C:\Temp\NLP\haaretz.heb'
    filesFirstCorpus = [f for f in listdir(sys.argv[1]) if isfile(os.path.join(sys.argv[1], f))]
    filesSecondCorpus = [f for f in listdir(sys.argv[2]) if isfile(os.path.join(sys.argv[2], f))]

    for name in filesFirstCorpus: #calculating Bigrams in  testset_literature start
        with open(sys.argv[1] + '\\' + name, encoding="utf8") as fileForWordsCount:
            words = [word for line in fileForWordsCount for word in line.split()]
            # wordsTotal=wordsTotal+Counter(words)
            # Counting words for every file and su,,arize it with previous value - testset_literature
            wordsTotal = wordsTotal + len(words)
            wordsTotalCorpus1 = wordsTotalCorpus1 + len(words)

        #Calculating P(word) - frequency at corpus - START
        for everyElement in words:
         if everyElement in frequencyOfEachWord.keys():
            frequencyOfEachWord[everyElement]+=1
         else:
            frequencyOfEachWord[everyElement]=1

         if everyElement in frequencyOfEachWordCorpus1.keys():
            frequencyOfEachWordCorpus1[everyElement]+=1
         else:
            frequencyOfEachWordCorpus1[everyElement]=1
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

         if tuple(everyElement) in bigramsCorpus1.keys():
            bigramsCorpus1[tuple(everyElement)]+=1
         else:
            bigramsCorpus1[tuple(everyElement)]=1
            bigramsTotalCorpus1+=1
         bigramFile.close()

    for name in filesSecondCorpus: #calculating Bigrams in  haaretz.heb start
        with open(sys.argv[2] + '\\' + name, encoding="utf8") as f:
            words = [word for line in f for word in line.split()]
            # wordsTotal = wordsTotal + Counter(words)
            # Counting words for every file and su,,arize it with previous value - haaretz.heb
            wordsTotal = wordsTotal + len(words)
            wordsTotalCorpus2 = wordsTotalCorpus2 + len(words)

        #Calculating P(word) - frequency at corpus - START
        for everyElement in words:
         if everyElement in frequencyOfEachWord.keys():
            frequencyOfEachWord[everyElement]+=1
         else:
            frequencyOfEachWord[everyElement]=1

         if everyElement in frequencyOfEachWordCorpus2.keys():
            frequencyOfEachWordCorpus2[everyElement]+=1
         else:
            frequencyOfEachWordCorpus2[everyElement]=1
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

         if tuple(everyElement) in bigramsCorpus2.keys():
            bigramsCorpus2[tuple(everyElement)]+=1
         else:
            bigramsCorpus2[tuple(everyElement)]=1
            bigramsTotalCorpus2+=1
    file = io.open('freq_raw.txt', 'w+', encoding='utf8')       # saving: freq_raw.txt CORPUSES
    for key,value in sorted(bigrams.items(), key=lambda x: (x[1], x[0])):
      file.write(str(key)+" "+str(float("{0:.3f}".format((value/wordsTotal)*1000)))+"\n") #multiply by 1000
    file.close()
    file = io.open('freq_raw_corpus1.txt', 'w+', encoding='utf8')       # saving: freq_raw_corpus1.txt CORPUS1
    for key,value in sorted(bigramsCorpus1.items(), key=lambda x: (x[1], x[0])):
      file.write(str(key)+" "+str(float("{0:.3f}".format((value/wordsTotalCorpus1)*1000)))+"\n") #multiply by 1000
    file.close()
    file = io.open('freq_raw_corpus2.txt', 'w+', encoding='utf8')       # saving: freq_raw_corpus1.txt CORPUS2
    for key,value in sorted(bigramsCorpus2.items(), key=lambda x: (x[1], x[0])):
      file.write(str(key)+" "+str(float("{0:.3f}".format((value/wordsTotalCorpus2)*1000)))+"\n") #multiply by 1000
    file.close()
pass

if len(sys.argv) != 4: # validate arguments length before continuing ##############################################
    sys.exit('Invalid argument number!, please make sure you run the the command as follow: '
                 'python hw2.py <FolderWithInputFiles1>  <FolderWithInputFiles2>  <FolderForOutputFiles>')
# validate arguments length before continuing #####################################################################

if __name__ == "__main__":
    ##### Questions 1-5 results
    calculate_Unigrams(sys.argv)
    calculatePMIBigrams()
    calculateTtestBigrams()
    calculateX2TestBigrams()
    calculateTrigrams(sys.argv)
    calculateTtestTrigramsA()
    calculateTtestTrigramsB()
    calculateX3TestTrigramsA()
    calculateX3TestTrigramsB()
    ##### Question 6 - results
    calculatePMIBigramsCorpus1()
    calculatePMIBigramsCorpus2()
    calculateTtestBigramsCorpus1()
    calculateTtestBigramsCorpus2()
    calculateX2TestBigramsCorpus1()
    calculateX2TestBigramsCorpus2()
    calculateTtestTrigramsACorpus1()
    calculateTtestTrigramsACorpus2()
    calculateX3TestTrigramsBCorpus1()
    calculateX3TestTrigramsBCorpus2()
    #calculateMutualCollacationsTrigram()
