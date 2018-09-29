# implementation of
# Hangman (game)
# https://en.wikipedia.org/wiki/Hangman_(game)

import random

LIMIT_TRIES = 6


def get_random_word():
    with open('top_1500_nouns.txt', 'r') as file:
        text = file.read()

    words = text.split('\n')

    return random.choice(words)


def game(word):
    # initial state
    hidden_word = ['_'] * len(word)
    guess_letters = []
    misses = 0

    # game loop
    while True:
        letter = input('Enter the letter: ')
        if letter in word:
            guess_letters.append(letter)
            hidden_word = [
                letter if letter in guess_letters else '_'
                for letter in word
            ]
            if '_' not in hidden_word:
                break
        else:
            misses += 1
            if misses == LIMIT_TRIES:
                break
            print(f'Try again. You have {LIMIT_TRIES - misses} more tries')

        print(''.join(hidden_word))

    # display resaults
    print('=' * 50)
    if '_' in hidden_word:
        print('Ooops! You lose!')
    else:
        print('Congratulation! You win!')
    print(f'The word was: {word}')
    print(f'You used: {misses}/{LIMIT_TRIES} tries')


word = get_random_word()
game(word)
