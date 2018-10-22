# 1
# Create a function decorator that prints the name of the current running
# function by using the __name__ attribute. Make sure to also decorate some
# different functions to see that it works properly.


def who_are_you(func):

    def wrapper(*args, **kwargs):
        print(f'call func: {func.__name__}')

        result = func(*args, **kwargs)
        return result

    return wrapper


@who_are_you
def say_hi(name):
    return f'Hi, {name}'


@who_are_you
def say_hello(name):
    return f'Hello, {name}'


print(say_hi('Dmytro'))
print(say_hello('Galyna'))
