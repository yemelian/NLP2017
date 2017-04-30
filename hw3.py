import sys, itertools
import csv
from copy import deepcopy
from sklearn import tree
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
import string
import re

result = {}
featureVectorsBeatles=[]
featureVectorsBreatney=[]

def get_lyrics_from_csv_by_artist(lyrics_file_name, artists, maximum_songs_number):
    """
    :param lyrics_file_name: lyrics csv file name to be parsed
    :param artists: list of artist
    :param maximum_songs_number: maximum song number to be retrieved for each artist
    :return: lyrics of the artists dictionary { "artist": [lyric1, lyric2,..], "artist2": [...] }
    """
    global result
    fieldnames = ['index', 'song', 'year', 'artist', 'genre', 'lyrics']
    d = {}
    for fn in fieldnames:
        d[fn] = []

    dict_reader = csv.DictReader(open(lyrics_file_name, 'r', encoding='utf8'), fieldnames=fieldnames, delimiter=',',
                                 quotechar='"')

    for row in dict_reader:
        for key in row:
            d[key].append(row[key])

    result = {}

    # loop over artists and retrieve each one's lyrics
    for artist_idx in range(len(artists)):

        lyrics = []
        songs_retrieved = 0
        artist = artists[artist_idx]

        for index in range(len(d["artist"])):
            # skip first index, since it is the column name e.g (index, genre, artist..)
            if index == 0:
                continue
            if d["artist"][index] == artist:
                ++songs_retrieved
                # break the artist's inner loop
                if songs_retrieved > maximum_songs_number:
                    break
                else:
                    # lyrics.append(d["lyrics"][index])
                    lyrics.append(d["lyrics"][index].replace('\n', ' '))

        result[artist] = lyrics

pass


def split_and_remove_punctuations(lyrics):

    lyrics = lyrics.split()

    for i in range(len(lyrics)):
        lyrics[i] = lyrics[i].strip(string.punctuation)

    return lyrics
pass


def featureVectorBuild(argv):
    global featureVectorsBeatles
    global featureVectorsBreatney
    wordsTop50 = []
    wordsTop50ToCheck={}
    with open(argv[2], "r") as fileTop50:
        for line in fileTop50.readlines():
            wordsTop50.append(line.replace("\n", "").replace("'", "").replace(",", ""))
        fileTop50.close()
    for element in wordsTop50:
        wordsTop50ToCheck[element] = 0

    # Beatles
    resultsForBeatles=result["beatles"]
    for lyricToCheck in resultsForBeatles:
        wordsTop50ToCheckTemp = wordsTop50ToCheck
        lyricToCheckList = split_and_remove_punctuations(lyricToCheck)
        for key, value in wordsTop50ToCheckTemp.items():
            for lyricToken in lyricToCheckList:
                if (key.strip().lower().replace('\'', '')) in (lyricToken.strip().lower()):
                    wordsTop50ToCheckTemp[key] = 1
        featureVectorToAdd = deepcopy(wordsTop50ToCheckTemp)
        featureVectorsBeatles.insert(len(featureVectorsBeatles), featureVectorToAdd)
        for element in wordsTop50ToCheckTemp:
            wordsTop50ToCheckTemp[element] = 0


    # Britney
    resultsForBreatney=result["britney-spears"]
    for lyricToCheck in resultsForBreatney:
        wordsTop50ToCheckTemp = wordsTop50ToCheck
        lyricToCheckList = split_and_remove_punctuations(lyricToCheck)
        for key, value in wordsTop50ToCheckTemp.items():
            for lyricToken in lyricToCheckList:
                if (key.strip().lower().replace('\'', '')) in (lyricToken.strip().lower()):
                    wordsTop50ToCheckTemp[key] = 1
        featureVectorToAdd = deepcopy(wordsTop50ToCheckTemp)
        featureVectorsBreatney.insert(len(featureVectorsBreatney), featureVectorToAdd)
        for element in wordsTop50ToCheckTemp:
            wordsTop50ToCheckTemp[element] = 0

pass

def ClassifierSVM():
    modelSVM = SVC()

pass

def ClassifierNaiveBaseMultinomial():
    modelNB = MultinomialNB()

pass

def ClassifierDTree():
    modelDTree = tree.DecisionTreeClassifier()

pass

def ClassifierKNN():
    modelNB = KNeighborsClassifier()

pass

def feature_classification(argv):

    #if len(sys.argv) != 4:
    #   sys.exit('Invalid argument number!, please make sure you run the the command as follow: python hw3.py'
    #             '<input_file> <words_file_input_path> <best_words_file_output_path>')

    # lyrics file
    lyrics_file_name = str(sys.argv[1])
    get_lyrics_from_csv_by_artist(lyrics_file_name, ["beatles", "britney-spears"], 400)

pass

if __name__ == "__main__":
    ##### Questions 1a-1b results
    feature_classification(sys.argv)
    featureVectorBuild(sys.argv)
    ##### Questions 1c results
    ClassifierSVM() #SVM(SVC)
    ClassifierNaiveBaseMultinomial()  #Naive Bayes(MultinomialNB)
    ClassifierDTree()  #DecisionTree(DecisionTreeClassifier)
    ClassifierKNN() #KNN(KNeighborsClassifier)
