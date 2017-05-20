import sys
import nltk
from copy import deepcopy
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import xml.etree.ElementTree as ET
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, ENGLISH_STOP_WORDS
from sklearn.feature_selection import SelectKBest
from gensim import models

tokensForFeatures={}
all_instances= []

def ClassifierLinearRegression(data_points, true_values):
    trained_svc = LogisticRegression().fit(data_points, true_values)
    scores = cross_val_score(trained_svc, data_points, true_values, cv=10)
    print("accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
pass

def featureVectorBuild(argv):
    global all_instances
    global tokensForFeatures
    contextData = ""

    #content from line.data.TEST.xml
    etree = ET.parse(str(sys.argv[1]))
    root = etree.getroot()
    instances = root.findall(".//instance")
    for element in instances:
        for child in element.iter():
            if child.tag == "context":
                for everyChild in child.iter():
                    contextData += everyChild.text.replace("\n", "").replace("'", "").replace(",", "")+" "

    #content from line.data.TRAIN.xml
    etree = ET.parse(str(sys.argv[2]))
    root = etree.getroot()
    instances = root.findall(".//instance")
    for element in instances:
        for child in element.iter():
            if child.tag == "context":
                for everyChild in child.iter():
                    contextData += everyChild.text.replace("\n", "").replace("'", "").replace(",", "")+" "
    #tokenization process
    tokensForFeatures=nltk.word_tokenize(contextData.strip())
    tokensForFeatures = nltk.FreqDist(tokensForFeatures)
pass

def feature_classification(argv):
    # build true values vector
    true_values = ["beatles" for x in range(len(lyrics_by_artist_dic['beatles']))]
    true_values.extend(["britney-spears" for x in range(len(lyrics_by_artist_dic['britney-spears']))])

    # merge lyrics together
    data = []
    #data.extend(lyrics_by_artist_dic["beatles"])
    #data.extend(lyrics_by_artist_dic["britney-spears"])

    #data = [var for var in data if var]

    # apply CountVectonizer and tf-idf
    count_vectorizer = CountVectorizer(stop_words=ENGLISH_STOP_WORDS, vocabulary=voc)
    transformer = TfidfTransformer()
    feature_vectors = transformer.fit_transform(count_vectorizer.fit_transform(data).toarray()).toarray()

    print("---------------------")
    print("Linear Regression:")
    ClassifierLinearRegression(feature_vectors, true_values)
    print("---------------------")
pass

def loadEmbeddingsFile(argv):
    # Loading: wiki.en.100k.vec
    w=models.KeyedVectors.load_word2vec_format('wiki.en.100k.vec', binary=False)
pass

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit('Invalid argument number!, please make sure you run the the command as follow: python hw4.py'
                 '<input_file> <words_file_input_path> <best_words_file_output_path>')

    # Question number 1
    featureVectorBuild(sys.argv)
    feature_classification(sys.argv)

    # Question number 2
    #loadEmbeddingsFile(sys.argv)

