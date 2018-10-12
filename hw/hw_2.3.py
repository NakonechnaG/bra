# 1
# Method overloading.
# Create a base class named Animal with a method called talk and then create
# two subclasses: Dog and Cat, and make their own implementation of the method
# talk be different. For instance Dog’s can be to print ‘voff voff’, while
# Cat’s can be to print ‘meow’


class Animal:

    def __init__(self, name):
        self.name = name

    # Abstract method
    def talk(self):
        raise NotImplementedError('Must be imlemented by  sub class')


class Dog(Animal):

    def talk(self):
        print('Woof Woof')


class Cat(Animal):

    def talk(self):
        print('Meow')


animals = [Cat('Siri'), Dog('Indi'), Dog('Ralf')]

for animal in animals:
    animal.talk()
    