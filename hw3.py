import sys
import itertools
import io
import csv
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


def get_lyrics_from_csv_by_artist(lyrics_file_name, artists, maximum_songs_number):
    """
    :param lyrics_file_name: lyrics csv file name to be parsed
    :param artists: list of artist
    :param maximum_songs_number: maximum song number to be retrieved for each artist
    :return: lyrics of the artists dictionary { "artist": [lyric1, lyric2,..], "artist2": [...] }
    """
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
    featureVectorsIncrementedBeatles = []
    featureVectorsAccumuletedBreatney = []
    wordsTop50 = []
    wordsTop50ToCheck = {}
    wordsTop50ToCheckAccumuleted = {}
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
            wordsTop50ToCheckAccumuleted[key] = lyricToCheck.count(key)
        featureVectorToAdd = deepcopy(wordsTop50ToCheckTemp)
        featureVectorAccumuletedToAdd = deepcopy(wordsTop50ToCheckAccumuleted)
        featureVectorsBeatles.insert(len(featureVectorsBeatles), featureVectorToAdd)
        featureVectorsIncrementedBeatles.insert(len(featureVectorsIncrementedBeatles), featureVectorAccumuletedToAdd)
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
            wordsTop50ToCheckAccumuleted[key] = lyricToCheck.count(key)
        featureVectorToAdd = deepcopy(wordsTop50ToCheckTemp)
        featureVectorAccumuletedToAdd = deepcopy(wordsTop50ToCheckAccumuleted)
        featureVectorsBreatney.insert(len(featureVectorsBreatney), featureVectorToAdd)
        featureVectorsAccumuletedBreatney.insert(len(featureVectorsAccumuletedBreatney), featureVectorAccumuletedToAdd)
        for element in wordsTop50ToCheckTemp:
            wordsTop50ToCheckTemp[element] = 0

    return featureVectorsBeatles, featureVectorsBreatney, featureVectorsIncrementedBeatles, featureVectorsAccumuletedBreatney

pass


def ClassifierSVM(data_points, true_values):
    trained_svc = SVC().fit(data_points, true_values)
    scores = cross_val_score(trained_svc, data_points, true_values, cv=10)
    print("accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

pass


def ClassifierNaiveBaseMultinomial(data_points, true_values):
    trained_model_nb = MultinomialNB().fit(data_points, true_values)
    scores = cross_val_score(trained_model_nb, data_points, true_values, cv=10)
    print("accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

pass


def ClassifierDTree(data_points, true_values):
    trained_model_tree = tree.DecisionTreeClassifier().fit(data_points, true_values)
    scores = cross_val_score(trained_model_tree, data_points, true_values, cv=10)
    print("accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

pass


def ClassifierKNN(data_points, true_values):
    model_knn = KNeighborsClassifier().fit(data_points, true_values)
    scores = cross_val_score(model_knn, data_points, true_values, cv=10)
    print("accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

pass


def feature_classification(argv):

    # lyrics file
    lyrics_file_name = str(sys.argv[1])
    lyrics_by_artist_dic = get_lyrics_from_csv_by_artist(lyrics_file_name, ["beatles", "britney-spears"], 400)

    # feature vector lyrics of top50 beatles and britney
    feature_vector_a, feature_vector_b, feature_vector_a_accumulated, feature_vector_b_accumulated = featureVectorBuild(argv, lyrics_by_artist_dic)

    # build true values vector
    true_values = ["beatles" for x in range(len(feature_vector_a))]
    true_values.extend(["britney-spears" for x in range(len(feature_vector_b))])
    true_values_accumulated = ["beatles" for x in range(len(feature_vector_a_accumulated))]
    true_values_accumulated.extend(["britney-spears" for x in range(len(feature_vector_b_accumulated))])

    # merge both feature vectors
    feature_vector_a.extend(feature_vector_b)
    feature_vector_a_accumulated.extend(feature_vector_b_accumulated)

    feature_vector = []
    for index in range(len(feature_vector_a)):
        feature_vector.append([v for k, v in feature_vector_a[index].items()])
    feature_vector_accumulated = []
    for index in range(len(feature_vector_a_accumulated)):
        feature_vector_accumulated.append([v for k, v in feature_vector_a_accumulated[index].items()])

    print("#####################")
    print("1. Running 'bag of words' on top50 given words once with binaries fv and one more with occurrences number fv")
    print("#####################")
    print("---------------------")
    print("SVM:")
    ClassifierSVM(feature_vector, true_values)
    print("Accumulated SVM:")
    ClassifierSVM(feature_vector_accumulated, true_values_accumulated)
    print("---------------------")
    # Naive Bayes(MultinomialNB)
    print("NB:")
    ClassifierNaiveBaseMultinomial(feature_vector, true_values)
    print("Accumulated NB:")
    ClassifierNaiveBaseMultinomial(feature_vector_accumulated, true_values_accumulated)
    print("---------------------")
    # DecisionTree(DecisionTreeClassifier)
    print("DTree:")
    ClassifierDTree(feature_vector, true_values)
    print("Accumulated DTree:")
    ClassifierDTree(feature_vector_accumulated, true_values_accumulated)
    print("---------------------")
    # KNN(KNeighborsClassifier)
    print("KNN:")
    ClassifierKNN(feature_vector, true_values)
    print("Accumulated KNN:")
    ClassifierKNN(feature_vector_accumulated, true_values_accumulated)
    print("---------------------\n")

pass


def bag_of_words(argv, voc=None):
    # lyrics file
    lyrics_file_name = str(sys.argv[1])
    lyrics_by_artist_dic = get_lyrics_from_csv_by_artist(lyrics_file_name, ["beatles", "britney-spears"], 400)

    # build true values vector
    true_values = ["beatles" for x in range(len(lyrics_by_artist_dic['beatles']))]
    true_values.extend(["britney-spears" for x in range(len(lyrics_by_artist_dic['britney-spears']))])

    # merge lyrics together
    data = []
    data.extend(lyrics_by_artist_dic["beatles"])
    data.extend(lyrics_by_artist_dic["britney-spears"])

    # apply CountVectonizer and tf-idf
    count_vectorizer = CountVectorizer(stop_words=ENGLISH_STOP_WORDS, vocabulary=voc)
    transformer = TfidfTransformer()
    feature_vectors = transformer.fit_transform(count_vectorizer.fit_transform(data).toarray()).toarray()

    print("#####################")
    if voc is None:
        print("2. Running bag of words on all words in the lyrics:")
    else:
        print("4. Running bag of words on selected best features:")
    print("#####################")
    print("---------------------")
    print('Number of unique words: ' + str(len(feature_vectors[0])))
    print("---------------------")

    # Questions 1a - 1f
    print("---------------------")
    print("SVM:")
    ClassifierSVM(feature_vectors, true_values)
    print("---------------------")
    # Naive Bayes(MultinomialNB)
    print("NB:")
    ClassifierNaiveBaseMultinomial(feature_vectors, true_values)
    print("---------------------")
    # DecisionTree(DecisionTreeClassifier)
    print("DTree:")
    ClassifierDTree(feature_vectors, true_values)
    print("---------------------")
    # KNN(KNeighborsClassifier)
    print("KNN:")
    ClassifierKNN(feature_vectors, true_values)
    print("---------------------\n")

pass


def select_k_best(argv, k_best=50):

    # lyrics file
    lyrics_file_name = str(argv[1])
    lyrics_by_artist_dic = get_lyrics_from_csv_by_artist(lyrics_file_name, ["beatles", "britney-spears"], 400)

    # build true values vector
    true_values = ["beatles" for x in range(len(lyrics_by_artist_dic['beatles']))]
    true_values.extend(["britney-spears" for x in range(len(lyrics_by_artist_dic['britney-spears']))])

    # merge lyrics together
    data = []
    data.extend(lyrics_by_artist_dic["beatles"])
    data.extend(lyrics_by_artist_dic["britney-spears"])

    # apply CountVectonizer and tf-idf
    count_vectorizer = CountVectorizer(stop_words=ENGLISH_STOP_WORDS)
    transformer = TfidfTransformer()
    feature_vectors = transformer.fit_transform(count_vectorizer.fit_transform(data).toarray()).toarray()
    k_best_select = SelectKBest(k=k_best)
    k_best_select.fit_transform(feature_vectors, true_values)

    k_best_words = np.asarray(count_vectorizer.get_feature_names())[k_best_select.get_support()]

    file_output_path = str(argv[3])
    file = io.open(file_output_path, 'w+', encoding='utf8')

    for word in k_best_words:
        file.write("'" + word + "'," + "\n")
    file.close()

    return k_best_words

pass


def custom_classification(argv):

    # lyrics file
    lyrics_file_name = str(argv[1])
    lyrics_by_artist_dic = get_lyrics_from_csv_by_artist(lyrics_file_name, ["etta-james", "bob-dylan"], 400)

    # build true values vector
    true_values = ["etta-james" for x in range(len(lyrics_by_artist_dic['etta-james']))]
    true_values.extend(["bob-dylan" for x in range(len(lyrics_by_artist_dic['bob-dylan']))])

    # merge lyrics together
    data = []
    data.extend(lyrics_by_artist_dic["etta-james"])
    data.extend(lyrics_by_artist_dic["bob-dylan"])

    # apply CountVectonizer and tf-idf
    count_vectorizer = CountVectorizer(stop_words=ENGLISH_STOP_WORDS)
    transformer = TfidfTransformer()
    feature_vectors = transformer.fit_transform(count_vectorizer.fit_transform(data).toarray()).toarray()
    k_best_select = SelectKBest(k=50)
    k_best_select.fit_transform(feature_vectors, true_values)

    k_best_words = np.asarray(count_vectorizer.get_feature_names())[k_best_select.get_support()]

    file_output_path = str("wordsCustom.txt")
    file = io.open(file_output_path, 'w+', encoding='utf8')

    for word in k_best_words:
        file.write("'" + word + "'," + "\n")
    file.close()

    words30 = []
    with open("love30words.txt", "r") as file30:
        for line in file30.readlines():
            words30.append(line.replace("\n", "").replace("'", "").replace(",", ""))
            file30.close()


    # apply CountVectonizer and tf-idf
    count_vectorizer = CountVectorizer(stop_words=ENGLISH_STOP_WORDS, vocabulary=words30)
    transformer = TfidfTransformer()
    feature_vectors = transformer.fit_transform(count_vectorizer.fit_transform(data).toarray()).toarray()

    print("#####################")
    print("5. Running bag of words on selected love words as features:")
    print("#####################")
    print("---------------------")
    print("SVM:")
    ClassifierSVM(feature_vectors, true_values)
    print("---------------------")
    # Naive Bayes(MultinomialNB)
    print("NB:")
    ClassifierNaiveBaseMultinomial(feature_vectors, true_values)
    print("---------------------")
    # DecisionTree(DecisionTreeClassifier)
    print("DTree:")
    ClassifierDTree(feature_vectors, true_values)
    print("---------------------")
    # KNN(KNeighborsClassifier)
    print("KNN:")
    ClassifierKNN(feature_vectors, true_values)
    print("---------------------\n")


pass

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit('Invalid argument number!, please make sure you run the the command as follow: python hw3.py'
                 '<input_file> <words_file_input_path> <best_words_file_output_path>')

    feature_classification(sys.argv)
    bag_of_words(sys.argv)
    k_best_words = select_k_best(sys.argv, 50)
    bag_of_words(sys.argv, k_best_words)
    custom_classification(sys.argv,)

