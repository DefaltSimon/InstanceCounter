# coding=utf-8

__author__ = "DefaltSimon"
__version__ = "0.1"


class SimpleCounter(type):
    """
    Used as a metaclass to count the instances of a class.
    Does not distinguish between classes.

    Use SimpleCounter._count or YourClass._count to get the count
    """
    _count = 0

    def __call__(cls, *args, **kwargs):
        instance = super(SimpleCounter, cls).__call__(*args, **kwargs)

        SimpleCounter._count += 1
        cls._count = SimpleCounter._count

        return instance


class Counter(type):
    """
    Used as a metaclass to count the instances of a class.
    DOES distinguish between classes

    Use Counter.classes[cls] or YourClass._count to get the count
    """
    _classes = {}

    def __call__(cls, *args, **kwargs):
        instance = super(Counter, cls).__call__(*args, **kwargs)

        if not Counter._classes.get(cls):
            Counter._classes[cls] = 1
        else:
            Counter._classes[cls] += 1

        cls._count = Counter._classes[cls]

        return instance
