import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *


def preprocessing_multiple_users(dir, users):
    # read all tweets as a string and integrate them

    # input: a list of users
    # output: a list which contains lists with words after tokenize and stemming
    documents = []
    documents_stemmed = []
    username = []
    for user in users:
        document = read_file_as_str(dir, user['_id'])
        documents.append(document)
        username.append(user['_id'])
    for doc in documents:
        tokens = get_tokens(doc)
        filtered_tokens = [w for w in tokens if w not in stopwords.words('english')]
        stemmer = PorterStemmer()
        stemmed = stem_tokens(filtered_tokens, stemmer)
        documents_stemmed.append(stemmed)
    return documents_stemmed, username


def read_file_as_str(dir, user):
    if not os.path.isfile('output/' + dir + '/' + user + "_user_timeline.txt"):
        raise TypeError('output/' + dir + '/' + user + "_user_timeline.txt" + " does not exist!")
    all_the_text = open('output/' + dir + '/' + user + "_user_timeline.txt").read()
    return all_the_text


def get_tokens(text):
    lowers = text.lower()
    # Remove the punctuation using the character deletion step of translate
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lowers.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed
