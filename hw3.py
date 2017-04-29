import sys
import csv


def get_yrics_of_beatles_and_britney_spears(lyrics_file_name):
    fieldnames = ['index', 'song', 'year', 'artist', 'genre', 'lyrics']
    d = {}
    for fn in fieldnames:
        d[fn] = []

    dict_reader = csv.DictReader(open(lyrics_file_name, 'r', encoding='utf8'), fieldnames=fieldnames, delimiter=',',
                                 quotechar='"')

    for row in dict_reader:
        for key in row:
            d[key].append(row[key])
    print(d)

    # loop over dictionary and retrieve beatles and britney spears lyrics
pass


def feature_classification(argv):

    #if len(sys.argv) != 4:
    #   sys.exit('Invalid argument number!, please make sure you run the the command as follow: python hw3.py'
    #             '<input_file> <words_file_input_path> <best_words_file_output_path>')

    # lyrics file
    lyrics_file_name = str(sys.argv[1])
    get_yrics_of_beatles_and_britney_spears(lyrics_file_name)

pass

if __name__ == "__main__":
    ##### Questions 1 results
    feature_classification(sys.argv)