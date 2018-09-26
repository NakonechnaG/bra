# 1
# A simple function.
# Create a simple function called favourite_movie, which takes a string
# containing the name of your favourite movie. The function should then print
# “My favourite movie is name”.


def favourite_movie(name):
    print('My favorite movie is {}'.format(name))


favourite_movie('Ace Ventura: Pet Detective')

# 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and
# capital as parameters. Then create a dictionary from those parameters, with
# ‘name’ and ‘capital’ as keys. Make the function print out the values of the
# dictionary to make sure that it works as intended.


def make_country(name, capital):
    country = {}
    country['name'] = name
    country['capital'] = capital

    return country


def show_country(country):
    print(','.join(country.values()))


country = make_country('Canada', 'Toronto')
show_country(country)


# 3
# A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic
# operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’
# or ‘*’) and an arbitrary number of arguments (only numbers) as second
# parameter. Then return the sum or product of all the numbers in the
# arbitrary parameter. For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# The call make_operation(‘-’, 5, 5, -10, -20) should return 30
# The call make_operation(‘*’, 7, 6) should return 42

from operator import add, sub, mul, truediv

support_operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}


def make_operation(operator_str, sequence):
    operator = support_operations.get(operator_str)
    result = sequence[0]

    for num in sequence[1:]:
        result = operator(result, num)
    return result


print(make_operation('+', [7, 7, 2]))
print(make_operation('-', [5, 5, -10, -20]))
print(make_operation('*', [7, 6]))
print(make_operation('/', [156, 12]))
