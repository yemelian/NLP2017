import sys,os,math,io, itertools


def featureClassification(argv):
    # Get 50 english words
    wordsTop50 = []
    #fileTop50 = io.open(sys.argv[2], 'w+', encoding='utf8')
    with open(sys.argv[2], "r") as fileTop50:
        for line in fileTop50.readlines():
            wordsTop50.append(line.replace("\n", ""))
    fileTop50.close()
    # Get 400 songs
    #songsToProcess = io.open(sys.argv[1], 'w+', encoding='utf8')
    with open(sys.argv[1], "r", encoding='utf8') as songsToProcess:
        for line in songsToProcess.readline():
          print(line)
    songsToProcess.close()

    pass

if len(sys.argv) != 4: # validate arguments length before continuing ##############################################
    sys.exit('Invalid argument number!, please make sure you run the the command as follow: '
                 'python hw3.py <input_file> <words_file_input_path> <best_words_file_output_path>')
   # validate arguments length before continuing #####################################################################

if __name__ == "__main__":
    ##### Questions 1 results
  featureClassification(sys.argv)
