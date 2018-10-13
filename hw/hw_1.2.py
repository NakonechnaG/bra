# 1
# The greeting program.
# Make a program that has your name and the current day of the week stored as 
# separate variables and then prints a message like this:
# Good day <name>! <day> is a perfect day to learn some python.
# where <name> and <day> are your predefined variables.

name = 'Lilu'
date = '09.09.18'
print('Good day {name} ! {} is a perfect day to learn some python'.format(date, name=name))

# 2
# Manipulate strings.
# Save your first and last name as separate variables, then use string
# concatenation to add them together with a white space in between and print
# a greeting.

name = 'Lilu'
surname = 'Joshua'
print(name + ' ' + surname)

# 3
# Using python as a calculator.
# Make a program with 2 numbers saved in separate variables a and b Then print
# the result for each of the following:
# Addition.
# Subtraction.
# Division.
# Multiplikation.
# Exponent (Power).
# Modulus.
# Floor division.

a, b = 20, 10
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} ** {b} = {a ** b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
