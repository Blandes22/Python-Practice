"""
This exercise is the first in a set of 3 that will result in a game of hangman
for the first exercise, we will pull text from the SOWPODS list of words and choose one
"""
from random import randint

def get_file(s: str):
    with open(s, 'r') as file:
        data = file.read().split('\n')

    return data

def get_word(words :list):
    n = randint(0, len(words))
    word = words[n]
    return word

if __name__ == "__main__":
    file_name = "sowpods.txt"
    word_list = get_file(file_name)
    print(get_word(word_list))