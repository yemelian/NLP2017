import sys, itertools
import csv
from copy import deepcopy
from sklearn import tree
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import string
import re


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
                if songs_retrieved < maximum_songs_number:
                    lyrics.append(d["lyrics"][index].replace('\n', ' '))
                    songs_retrieved += 1
                # break the artist's inner loop
                else:
                    break

        result[artist] = lyrics

    return result

pass


def split_and_remove_punctuations(lyrics):

    lyrics = lyrics.split()

    for i in range(len(lyrics)):
        lyrics[i] = lyrics[i].strip(string.punctuation)

    return lyrics
pass


def featureVectorBuild(argv, lyrics_by_artist_dic):
    featureVectorsBeatles = []
    featureVectorsBreatney = []
    wordsTop50 = []
    wordsTop50ToCheck={}
    with open(argv[2], "r") as fileTop50:
        for line in fileTop50.readlines():
            wordsTop50.append(line.replace("\n", "").replace("'", "").replace(",", ""))
        fileTop50.close()
    for element in wordsTop50:
        wordsTop50ToCheck[element] = 0

    # Beatles
    resultsForBeatles = lyrics_by_artist_dic["beatles"]
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
    resultsForBreatney = lyrics_by_artist_dic["britney-spears"]
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

    return featureVectorsBeatles, featureVectorsBreatney

pass


def ClassifierSVM(data_points, true_values):
    trained_svc = SVC().fit(data_points, true_values)
    scores = cross_val_score(trained_svc, data_points, true_values, cv=10)
    print("SVM accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

pass


def ClassifierNaiveBaseMultinomial(data_points, true_values):
    trained_model_nb = MultinomialNB().fit(data_points, true_values)
    scores = cross_val_score(trained_model_nb, data_points, true_values, cv=10)
    print("Naive Base accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

pass


def ClassifierDTree(data_points, true_values):
    trained_model_tree = tree.DecisionTreeClassifier().fit(data_points, true_values)
    scores = cross_val_score(trained_model_tree, data_points, true_values, cv=10)
    print("Decision tree accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

pass


def ClassifierKNN(data_points, true_values):
    model_knn = KNeighborsClassifier().fit(data_points, true_values)
    scores = cross_val_score(model_knn, data_points, true_values, cv=10)
    print("KNN accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

pass

def feature_classification(argv):

    #if len(sys.argv) != 4:
    #   sys.exit('Invalid argument number!, please make sure you run the the command as follow: python hw3.py'
    #             '<input_file> <words_file_input_path> <best_words_file_output_path>')

    # lyrics file
    lyrics_file_name = str(sys.argv[1])
    lyrics_by_artist_dic = get_lyrics_from_csv_by_artist(lyrics_file_name, ["beatles", "britney-spears"], 400)

    # feature vector lyrics of top50 beatles and britney
    feature_vector_a, feature_vector_b = featureVectorBuild(sys.argv, lyrics_by_artist_dic)

    # build true values vector
    true_values = ["beatles" for x in range(len(feature_vector_a))]
    true_values.extend(["britney-spears" for x in range(len(feature_vector_b))])

    # merge both feature vectors
    feature_vector_a.extend(feature_vector_b)

    feature_vector = []
    for index in range(len(feature_vector_a)):
        feature_vector.append([v for k, v in feature_vector_a[index].items()])


    # Questions 1c results
    # SVM(SVC)

    ClassifierSVM(feature_vector, true_values)

    # Naive Bayes(MultinomialNB)
    ClassifierNaiveBaseMultinomial(feature_vector, true_values)

    # DecisionTree(DecisionTreeClassifier)
    ClassifierDTree(feature_vector, true_values)

    # KNN(KNeighborsClassifier)
    ClassifierKNN(feature_vector, true_values)

pass

if __name__ == "__main__":
    ##### Questions 1a-1b results
    feature_classification(sys.argv)
