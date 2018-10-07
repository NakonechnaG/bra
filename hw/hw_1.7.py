# 1
# dict comprehension exercise.
# Make a program that given a whole sentence (a string) will make a dict
# containing all unique words as keys and the number of occurrences as values.

text = """
There are many variations of passages of Lorem Ipsum available, but the 
majority have suffered alteration in some form, by injected humour, or 
randomised words which don't look even slightly believable. If you are 
going to use a passage of Lorem Ipsum, you need to be sure there isn't 
anything embarrassing hidden in the middle of text. All the Lorem Ipsum 
generators on the Internet tend to repeat predefined chunks as necessary, 
making this the first true generator on the Internet. It uses a dictionary 
of over 200 Latin words, combined with a handful of model sentence structures, 
to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum 
is therefore always free from repetition, injected humour, or non-
characteristic words etc.
"""
words = text.lower().split()
uniq_words = {}
for word in words:
    count = uniq_words.get(word, 0)
    uniq_words[word] = count + 1
print(uniq_words)

# 2
# List comprehension exercise I.
# Consider the following list: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Now, make a program (no longer than one line) that makes a new list 
# containing all the values in a but no even numbers.

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([i for i in numbers if i % 2 != 0])

# 3
# List comprehension exercise II.
# Use a list comprehension to make a list containing tuples (i, j) 
# where i goes from 1 to 10 and j is corresponding i squared.

print([(i, i ** 2) for i in range(1, 10)])
