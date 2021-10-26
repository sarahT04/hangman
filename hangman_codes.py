from string import punctuation, digits
from itertools import islice
from random import randint

file_name = 'countries.txt'
file_len = 196  # please change this accordingly
random_index = randint(0, file_len)

with open(file_name) as lines:
    for line in islice(lines, random_index, random_index + 1):
        initial_word = line.strip()

indices = []
lives = 5

def hangmanizer(word, indices=False):
    # returns a string
    has_index = indices
    h_list = []
    for j, i in enumerate(word):
        if i == ' ' or i in punctuation or i in digits:
            h_list.append(i)
        elif has_index and j in indices:
            h_list.append(word[j])
        else:
            h_list.append('_')
    return ''.join(h_list)


def find_index(word, alphabet):
    # returns whether index was found or not, and if true append it to indices []
    word = list(word.lower())
    global indices
    found = False
    for j, i in enumerate(word):
        if i == alphabet:
            found = True
            indices.append(j)
    return found


def user_won(boolean):
    # returns a message when user loses or wins.
    if boolean:
        return f"You've won! Congrats! It took you {5 - lives} mistakes to complete."
    else:
        return f"Too bad. You lost. You'll get 'em next time. The word was: {initial_word}"
