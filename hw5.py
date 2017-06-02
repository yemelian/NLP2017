import os
import sys
import string
import numpy

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

## Getting Sentence from file to check
def checkSentence(sentenceToCheck):


 print(sentenceToCheck)
pass


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit('Invalid argument number!, please make sure you run the the command as follow: python parser.py'
                 '<grammar file>  <test_sentences file> <parses output>')

    grammar=getGrammar(sys.argv)


    with open(sys.argv[2], "r") as sentencesToCheck:
     for sentence in sentencesToCheck.readlines():
        checkSentence(sentence)
     sentencesToCheck.close()



