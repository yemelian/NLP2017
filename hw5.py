import os
import sys
import string
import numpy
from xml.etree import ElementTree

def getGrammar(argv):
    print("grammar")

pass


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit('Invalid argument number!, please make sure you run the the command as follow: python parser.py'
                 '<grammar file>  <test_sentences file> <parses output>')

    grammar=getGrammar(sys.argv)





