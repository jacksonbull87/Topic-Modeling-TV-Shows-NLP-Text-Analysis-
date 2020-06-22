
import nltk
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer


def text_preprocessor(string):
    #removes words more than 2 letters, stopwords, lemmatizes
    tokenize_review = string.split()
    word_list = []
    #let's remove any word that has less than 3 letters. this will 
    #take care of indefinite articles and former contractions that 
    #resulted in single letter words after removing punctuations.
    for word in tokenize_review:
        if len(word) > 2:
            word_list.append(word)
    #now let's remove english stopwords
    filtered_wordlist = []
    for word in word_list:
        if word not in stopwords.words('english'):
            filtered_wordlist.append(word)
    #now let's lemmatize each item so that words with similar 
    #inflections will be counted as one item
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for word in filtered_wordlist:
        lemmatized_words.append(lemmatizer.lemmatize(word))
    
    #returns processed string of words
    return ' '.join(lemmatized_words)