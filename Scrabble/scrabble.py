import sys
import itertools

class NoArgumentException(Exception):
    """Handle no argument excetion"""

    def __init__(self):
        Exception.__init__(self)

global possible_words, word_value
possible_words = []
word_value = []

def calculate(word):
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    total = 0

    for letter in word:
        total += scores[letter]

    word_value.append({'word':word,'total':total})

def generate(rack):
    for i in range(1, len(rack) + 1):
        word = itertools.permutations(rack, i)
        for j in word:
            possible_words.append(''.join(j))

if __name__ == '__main__':

    try:
        if len(sys.argv) < 2:
            raise NoArgumentException()

        rack = sys.argv[1].lower()
        generate(rack)
        f = open('sowpods.txt')
        for words in f:
            if words.replace('\n','').lower() in possible_words:
                calculate(words.replace('\n','').lower())
        f.close()

        sorted_list = sorted(word_value, key = lambda k: (k['total'], k['word']), reverse=True)
        for i in sorted_list:
            print(i['total'], i['word'])

    except NoArgumentException as nae:
        print('Usage: scrabble.py [RACK]')
