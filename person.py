#definition of a class
class Person:
    #members
    name = None
    age = None

    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print 'My name is %s' % self.name

    def say_age(self):
        print 'My age is %d' % self.age

    def have_birthday(self):
        self.age += 1