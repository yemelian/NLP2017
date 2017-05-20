import sys
import nltk
import string
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
wordsToCheck={}
contextDataList=[]
featureVectors = []
featureVectorsIncremented = []

def split_and_remove_punctuations(lyrics):

    lyrics = lyrics.split()

    for i in range(len(lyrics)):
        lyrics[i] = lyrics[i].strip(string.punctuation)

    return lyrics
pass

def ClassifierLinearRegression(data_points, true_values):
    trained_svc = LogisticRegression().fit(data_points, true_values)
    scores = cross_val_score(trained_svc, data_points, true_values, cv=10)
    print("accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
pass

def featureVectorBuild(argv):
    global all_instances
    global tokensForFeatures
    global contextDataList
    global featureVectors
    global featureVectorsIncremented
    wordsToCheckAccumuleted = {}
    contextData = ""
    ###############################################################################################################
    #START - getting all words for BAG OF WORDS [variable - wordsToCheck]
    #content from line.data.TEST.xml
    etree = ET.parse(str(sys.argv[1]))
    root = etree.getroot()
    instances = root.findall(".//instance")
    for element in instances:
        for child in element.iter():
            if child.tag == "context":
                for everyChild in child.iter():
                    contextData += everyChild.text.replace("\n", "").replace("'", "").replace(",", "")+" "
                    tempStr=everyChild.text.replace("\n", " ")
                    tempStr=tempStr.replace("\t", " ")
                    tempStr = tempStr.rstrip()
                    if tempStr != "":
                        contextDataList.append(tempStr)

    #content from line.data.TRAIN.xml
    etree = ET.parse(str(sys.argv[2]))
    root = etree.getroot()
    instances = root.findall(".//instance")
    for element in instances:
        for child in element.iter():
            if child.tag == "context":
                for everyChild in child.iter():
                    contextData += everyChild.text.replace("\n", "").replace("'", "").replace(",", "")+" "
                    tempStr = everyChild.text.replace("\n", " ")
                    tempStr = tempStr.replace("\t", " ")
                    tempStr = tempStr.rstrip()
                    if tempStr != "":
                        contextDataList.append(tempStr)
    #tokenization process
    tokensForFeatures=nltk.word_tokenize(contextData.strip())
    tokensForFeatures = nltk.FreqDist(tokensForFeatures)
    wordsToCheck =  nltk.FreqDist(tokensForFeatures)
    # all word that will be for check in feature vector
    for element in wordsToCheck:
        wordsToCheck[element] = 0
    #END - getting all words for BAG OF WORDS
    ##############################################################################################################

    # building feature vector with wordsToCheck
    wordsToCheckTemp = wordsToCheck
    for dataToCheck in contextDataList:
                dataToCheckList = split_and_remove_punctuations(dataToCheck)
                for element in wordsToCheckTemp:
                    wordsToCheckTemp[element] = 0
                for key, value in wordsToCheckTemp.items():
                    for dataToken in dataToCheckList:
                        if (key.strip().lower().replace('\'', '')) in (dataToken.strip().lower()):
                            wordsToCheckTemp[key] = 1
                   #wordsToCheckAccumuleted[key] = dataToCheck.count(key)
                featureVectorToAdd = deepcopy(wordsToCheckTemp)
                featureVectors.insert(len(featureVectors), featureVectorToAdd)
               #featureVectorAccumuletedToAdd = deepcopy(wordsToCheckAccumuleted)
               #featureVectorsIncremented.insert(len(featureVectorsIncremented), featureVectorAccumuletedToAdd)
pass

def feature_classification(argv):
    # build true values vector
    true_values = ["line" for x in range(len(tokensForFeatures))]

    feature_vector = []
    for index in range(len(tokensForFeatures)):
        feature_vector.append([v for k, v in tokensForFeatures[index].items()])


    print("---------------------")
    print("Linear Regression:")
    ClassifierLinearRegression(feature_vector, true_values)
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
    #feature_classification(sys.argv)
    #bag_of_words(sys.argv)

    # Question number 2
    #loadEmbeddingsFile(sys.argv)
