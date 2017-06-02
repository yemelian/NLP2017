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


def getGrammar(argv):
    print("grammar")

pass


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit('Invalid argument number!, please make sure you run the the command as follow: python parser.py'
                 '<grammar file>  <test_sentences file> <parses output>')

    grammar=getGrammar(sys.argv)





