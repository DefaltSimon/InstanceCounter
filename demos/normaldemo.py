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
        print("Amount of {} instances: {}".format(cls.__name__, cls._count))


class SomeOtherClass(metaclass=Counter):
    def __init__(self):
        print("Initialized SomeOtherClass")

    @classmethod
    def print_instance_count(cls):
        print("Amount of {} instances: {}".format(cls.__name__, cls._count))

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

# You can also get a list of instances of all class instances with:

# All instances of AnotherClass
another_class = (str(a) for a in Counter._instances.get(AnotherClass))
print("Instances of AnotherClass: {}".format(", ".join(another_class)))
# All instances of SomeOtherClass
some_class = (str(a) for a in Counter._instances.get(SomeOtherClass))
print("Instances of SomeOtherClass: {}".format(", ".join(some_class)))
