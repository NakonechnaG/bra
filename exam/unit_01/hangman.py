# implementation of
# Hangman (game)
# https://en.wikipedia.org/wiki/Hangman_(game)

import os
import random
from animation import draw_hangman

LIMIT_TRIES = 6


def get_random_word():
    with open('top_1500_nouns.txt', 'r') as file:
        text = file.read()

    words = text.split('\n')

    return random.choice(words)


def draw_frame(misses, word, used_letters):
    os.system('clear')

    print('-' * 50)
    draw_hangman(misses)
    if used_letters:
        print(f'Your used letters: {",".join(used_letters)}')
    else:
        print()
    print()
    print('Secret word:', ''.join(word))
    print()


def draw_message(message):
    print()
    print(message)
    input('Press enter to continue\n')


def game(word):
    # initial state
    hidden_word = ['_'] * len(word)
    guess_letters = []
    used_letters = []
    misses = 0

    # game loop
    while True:
        draw_frame(
            misses=misses,
            word=hidden_word,
            used_letters=used_letters,
        )

        answer = input('Enter the letter: ')
        answer = answer.strip()
        if answer == '-':
            break

        if len(answer) != 1:
            draw_message('Please, enter only one letter.')
            continue

        letter = answer.lower()
        if letter in guess_letters or letter in used_letters:
            draw_message('This letter has already used. Type another one.')
            continue

        if letter in word:
            guess_letters.append(letter)
            hidden_word = [
                letter if letter in guess_letters else '_'
                for letter in word
            ]
            if '_' not in hidden_word:
                break
        else:
            used_letters.append(letter)

            misses += 1
            if misses == LIMIT_TRIES:
                break

            draw_message(
                f'Try again. You have {LIMIT_TRIES - misses} more tries'
            )

    # display last frame
    draw_frame(
        misses=misses,
        word=hidden_word,
        used_letters=used_letters,
    )

    # display resaults
    print('=' * 50)
    if '-' == letter:
        print('You quit the game')
    elif '_' in hidden_word:
        print('Ooops! You lose!')
        print(f'Secret word was: {word}')
    else:
        print('Congratulation! You win!')
    print(f'You used: {misses}/{LIMIT_TRIES} tries')


word = get_random_word()
word = word.lower()
game(word)
