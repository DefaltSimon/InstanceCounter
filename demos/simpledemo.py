# coding=utf-8

# was in a folder called InstanceCounter, adapt your import!
from instancecount import SimpleCounter

# SimpleCounter demo
# SimpleCounter counts all classes as one


class AnotherClass(metaclass=SimpleCounter):
    def __init__(self):
        print("Initialized AnotherClass")

    @classmethod
    def print_instance_count(cls):
        print("Instances {}".format(cls._instances))


class SomeOtherClass(metaclass=SimpleCounter):
    def __init__(self):
        print("Initialized SomeOtherClass")

    @classmethod
    def print_instance_count(cls):
        print("Instances: {}".format(cls._instances))

# A simple class
a = AnotherClass()
b = AnotherClass()

# Prints the same
a.print_instance_count()
b.print_instance_count()

# A different class
c = SomeOtherClass()

# Is 3 because SimpleCounter does not distinguish between classes
c.print_instance_count()

# You can also get a list of instances of all the instances with:

print("Instances: {}".format(", ".join(str(a) for a in SimpleCounter._instances)))
