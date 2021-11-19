from collections import defaultdict
import string
import random


class Markov():
    def __init__(self, file_path):
        self.file_path = file_path

        self.text = self.remove_punctuations(self.get_text())
        self.model = self.model()

    def get_text(self):
        '''
        This function will read the input file and return the text associated to the file line by line in a list
        '''
        text = []
        for line in open(self.file_path):
            text.append(line)
        return ' '.join(text)

    def remove_punctuations(self, text):
        '''
        Given a string of text this function will return the same input text without any punctuations
        '''
        return text.translate(str.maketrans('', '', string.punctuation))

    def model(self):
        '''
        This function will take a block of text as the input and map each word in the text to a key where the
        values associated to that key are the words which proceed it
        args:
            text (String) : The string of text you wish to train your markov model around
        example:
            text = 'hello my name is V hello my name is G hello my current name is F world today is a good day'
            markov_model(text)
            >> {'F': ['world'],
                'G': ['hello'],
                'V': ['hello'],
                'a': ['good'],
                'current': ['name'],
                'good': ['day'],
                'hello': ['my', 'my', 'my'],
                'is': ['V', 'G', 'F', 'a'],
                'my': ['name', 'name', 'current'],
                'name': ['is', 'is', 'is'],
                'today': ['is'],
                'world': ['today']}
        '''

        # split the input text into individual words seperated by spaces
        words = self.text.split(' ')

        markov_dict = defaultdict(list)

        # create list of all word pairs
        for current_word, next_word in zip(words[0:-1], words[1:]):
            markov_dict[current_word].append(next_word)

        markov_dict = dict(markov_dict)
        print('Successfully Trained')
        return markov_dict


def predict_words(chain, first_word, number_of_words=5):
    '''
    Given the input result from the markov_model function and the nunmber of words, this function will allow you to predict the next word
    in the sequence

    args:
        chain (Dictionary) : The result of the markov_model function
        first_word (String) : The word you want to start your prediction from, note this word must be available in chain
        number_of_words (Integer) : The number of words you want to predict

    example:
        chain = markov_model(text)
        generate_sentence(chain, first_word = 'do', number_of_words = 3)
        >> Do not fail.
    '''

    if first_word in list(chain.keys()):
        word1 = str(first_word)

        predictions = word1.capitalize()

        # Generate the second word from the value list. Set the new word as the first word. Repeat.
        for i in range(number_of_words-1):
            word2 = random.choice(chain[word1])
            word1 = word2
            predictions += ' ' + word2

        # End it with a period
        predictions += '.'
        return predictions
    else:
        return "Word not in corpus"


if __name__ == '__main__':
    m = Markov(file_path='Shakespeare.txt')
    chain = m.model
    print(predict_words(chain, first_word='do', number_of_words=10))
