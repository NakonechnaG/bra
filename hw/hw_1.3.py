# 1
# The valid phone number program.
# Make a program that checks if a string is on the right format 
# for a phone number. The program should check that the string 
# contains only numerical characters and is only 10 characters long. 
# Print a suitable message depending on the outcome of the string evaluation.

phone = input('Pleas, enter your phon number : ')

if not phone.isdigit():
    print('The phone number is wrong, it must be only digit! ')
elif len(phone) != 10:
    print("Incorrect number of digit, it must be 10! ")
else:
    print('Congratulation! Phone is OK ')

# 2
# The math quiz program.
# Write a program that asks the answer for
# a mathematical expression, checks whether the user
# is right or wrong, and then responds with a message accordingly.

import random

a = random.randint(1, 10)
b = random.randint(1, 10)

answer = input(f'Make a calculation: {a} + {b} = ')
if a + b == int(answer):
    print('Yep! You are right!')
else:
    print('Nope! Try one more time')

# 3
# The name check.
# Write a program that has a variable with your name stored
# (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the
# stored name even if the given name has another case, e.g. 
# if your input is “Anton” and the stored name is “anton” it should
# return True.

name = ('galyna')

answer = input("Try to guess, what's my name?  ")
if name == answer.lower():
    print('Wow! You are rigft ')
else:
    print('Ooo no, maybe next time you better luck!')
