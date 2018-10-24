# 1
# Create a class Person that has at least attributes first_name and last_name,
# use property decorators to create getters and setters for the email and
# fullname, email should be first_name.last_name@email.com and fullname just
# first_name together with last_name separated by a space character.


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name.title() + ' ' + self.last_name.title()

    @property
    def email(self):
        return self.first_name + '.' + self.last_name + '@email.com'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split()
        self.first_name = first.title()
        self.last_name = last.title()


p = Person('lucas', 'first')
print(p)
print(p.full_name)
print(p.email)
p.full_name = 'miya wonder'
print(p.first_name, p.last_name)
