# 1
# Create a function that takes in 2 numbers and a mathematical function, that
# also takes 2 numbers as arguments, and then returns the result of the passed
# argument function given the 2 numbers.

from operator import add
from operator import mul
from operator import sub
from operator import truediv


def numbers(func, x, y):
    return func(x, y)


print('add(2, 40) =', numbers(add, 2, 40))
print('mul(2, 40) =', numbers(mul, 2, 21))
print('sub(2, 40) =', numbers(sub, 44, 2))
print('truediv(2, 40) =', numbers(truediv, 84, 2))
