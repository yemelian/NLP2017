import sys
import io
import nltk
from copy import deepcopy
from sklearn import tree
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, ENGLISH_STOP_WORDS
from sklearn.feature_selection import SelectKBest
import numpy as np
from gensim import models


def loadEmbeddingsFile(argv):

    # Loading: wiki.en.100k.vec
    w=models.KeyedVectors.load_word2vec_format('wiki.en.100k.vec', binary=False)

pass


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit('Invalid argument number!, please make sure you run the the command as follow: python hw4.py'
                 '<input_file> <words_file_input_path> <best_words_file_output_path>')

    loadEmbeddingsFile(sys.argv)
    sentence = "At eight o'clock on Thursday morning"
    tokens = nltk.word_tokenize(sentence)
