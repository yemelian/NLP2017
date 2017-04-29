import sys
import csv


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
                ++songs_retrieved
                # break the artist's inner loop
                if songs_retrieved > maximum_songs_number:
                    break
                else:
                    # lyrics.append(d["lyrics"][index])
                    lyrics.append(d["lyrics"][index].replace('\n', ' '))

        result[artist] = lyrics

    print(result)

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
    ##### Questions 1 results
    feature_classification(sys.argv)