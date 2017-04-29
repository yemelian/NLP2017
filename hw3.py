import sys
import csv


def get_lyrics_from_csv_by_artist(lyrics_file_name, artists):
    fieldnames = ['index', 'song', 'year', 'artist', 'genre', 'lyrics']
    d = {}
    for fn in fieldnames:
        d[fn] = []

    dict_reader = csv.DictReader(open(lyrics_file_name, 'r', encoding='utf8'), fieldnames=fieldnames, delimiter=',',
                                 quotechar='"')

    for row in dict_reader:
        for key in row:
            d[key].append(row[key])

    # loop over artists and retrieve each one's lyrics
    for artist_idx in range(len(artists)):
        artist = artists[artist_idx]
        for index in range(len(d["artist"])):
            # skip first index, sinnce it is the column name e.g (index,genere,artist..)
            if index == 0:
                continue
            if d["artist"][index] == artist:
                print(d["lyrics"][index])

    # print(d)
pass


def feature_classification(argv):

    #if len(sys.argv) != 4:
    #   sys.exit('Invalid argument number!, please make sure you run the the command as follow: python hw3.py'
    #             '<input_file> <words_file_input_path> <best_words_file_output_path>')

    # lyrics file
    lyrics_file_name = str(sys.argv[1])
    get_lyrics_from_csv_by_artist(lyrics_file_name, ["beatles", "britney-spears"])

pass

if __name__ == "__main__":
    ##### Questions 1 results
    feature_classification(sys.argv)