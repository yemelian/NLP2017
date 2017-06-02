import os
import sys
import nltk
import string
import numpy
from sklearn.metrics import accuracy_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn import svm, neighbors, tree, naive_bayes
from xml.etree import ElementTree
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, ENGLISH_STOP_WORDS
from sklearn.feature_selection import SelectKBest
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from gensim import models
from sklearn.preprocessing import MaxAbsScaler

grammarList={}

## Getting rammar from file
## Every member at dicionary:
## Value is probabillity mumber
## Key is a rule of form LeftSide"*"RightSide
## Example for  input 0.2 V -> stops will be: Value=0.2 Key=V*stops
def getGrammar(argv):
 global grammarList
 with open(argv[1], "r") as grammarFileData:
     for line in grammarFileData.readlines():
         newList=line.split("->")
         newValue=newList[0].split(" ")
         newKey=newValue[1].strip()+"*"+newList[1].strip()
         grammarList[newKey] = newValue[0]
     grammarFileData.close()
pass


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit('Invalid argument number!, please make sure you run the the command as follow: python parser.py'
                 '<grammar file>  <test_sentences file> <parses output>')

    grammar=getGrammar(sys.argv)





