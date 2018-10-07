# 1
# The Guessing Game.
# Write a program that generates a random number between 1 and 10 and let’s
# the user guess what number was generated. The result should be sent back to
# the user via a print statement.

import random

num = random.randint(1, 10)
answer = input('Try to guess, what number was generated from 1 to 10 ? ')
if int(answer) == int(num):
    print('WOW! You are seer! ')
else:
    print('Maybe next time you better luck ')

# 2
# The birthday greeting program.
# Write a program that takes your name as input, and then your age as input
# and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”

name = input("What's your name? ")
age = input('How old are you? ')
age = int(age) + 1 
print(f"Hello {name}, on your next Birthday you'll be {age} years ")
