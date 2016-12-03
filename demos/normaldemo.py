# coding=utf-8

# was in a folder called InstanceCounter, adapt your import!
from instancecount import Counter

# Counter demo
# Counter counts each class separately


class AnotherClass(metaclass=Counter):
    def __init__(self):
        print("Initialized AnotherClass")

    @classmethod
    def print_instance_count(cls):
        print("Amount of {} classes: {}".format(cls.__name__, cls._count))


class SomeOtherClass(metaclass=Counter):
    def __init__(self):
        print("Initialized SomeOtherClass")

    @classmethod
    def print_instance_count(cls):
        print("Amount of {} classes: {}".format(cls.__name__, cls._count))

# One class
a = AnotherClass()
b = AnotherClass()

# Prints the same
a.print_instance_count()
b.print_instance_count()

# A different class
c = SomeOtherClass()

# Is 1 because Counter DOES distinguish between classes
c.print_instance_count()
