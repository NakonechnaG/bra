# 1
# Make a program that generates a list that has all squared values of integers
# from 1 to 100, i.e., like this: [1, 4, 9, 16, 25, 36, …, 10000]

print([i ** 2 for i in range(1, 100)])


# 2
# Make a program that prompts the user to input the name of a car, the program
# should save the input in a list and ask for another, and then another, until
# the user inputs ‘q’, then the program should stop and the list of cars that
# was produced should be printed.

cars = []

while True:
    answer = input('Type a name of a car: ')
    if answer == 'q':
        break
    else:
        cars.append(answer)
print(cars)


# 3
# Start of with any list containing at least 10 elements, then print all
# elements in reverse order.

lst = [i for i in range(100, 110)]
for i in reversed(lst):
    print(i)
