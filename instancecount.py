# coding=utf-8

__author__ = "DefaltSimon"
__version__ = "0.1.1"


class SimpleCounter(type):
    """
    Used as a metaclass to count the instances of a class.
    Does not distinguish between classes.

    Use SimpleCounter._count or YourClass._count to get the count
    """
    _instances = []

    def __call__(cls, *args, **kwargs):
        instance = super(SimpleCounter, cls).__call__(*args, **kwargs)

        SimpleCounter._instances.append(instance)
        cls._instances = len(SimpleCounter._instances)

        return instance


class Counter(type):
    """
    Used as a metaclass to count the instances of a class.
    DOES distinguish between classes

    Use Counter.classes[cls] or YourClass._count to get the count
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        instance = super(Counter, cls).__call__(*args, **kwargs)

        if not Counter._instances.get(cls):
            Counter._instances[cls] = [instance]
        else:
            Counter._instances[cls].append(instance)

        cls._count = len(Counter._instances[cls])

        return instance
