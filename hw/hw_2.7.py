# 1
# Create a generator function that yields all squares of integers within a
# given range, i.e., arguments start and stop.


def squares(start, stop):
    for i in range(start, stop):
        yield i ** 2


for n in squares(1, 20):
    print(n)
