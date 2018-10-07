# 1

# Exclusive common numbers.
# Generate 2 lists of length 10 with random integers from 1 to 10, and make a
# third list containing the common integers between the 2 initial lists
# without any duplicates.

import random

list_one = [random.randint(1, 10) for i in range(10)]
list_two = [random.randint(1, 10) for i in range(10)]
common_elements = set(list_one) & set(list_two)
print('list_one', list_one)
print('list_two', list_two)
print('common_elements', common_elements)

# 2
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers
# from the list that are divisible by 7 but not a multiple of 5 and store them
# in a separate list. Finally print the list.

lst = [i for i in range(1, 100) if i % 7 == 0 and not i % 5 == 0]
print(lst)
