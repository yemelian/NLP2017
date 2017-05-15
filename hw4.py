import nltk


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit('Invalid argument number!, please make sure you run the the command as follow: python hw4.py'
                 '<line.data.train> <line.data.test> <output>')
    sentence = """At eight o'clock on Thursday morning
    tokens = nltk.word_tokenize(sentence)
