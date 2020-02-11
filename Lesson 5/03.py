"""Module with Observable class"""


class Observable:
    """Parent class"""
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return "{}".format(
            {a: getattr(self, a) for a in dir(self) if not a.startswith('__')})

    def __getattr__(self, item):
        return self[item]


class X(Observable):
    """Some derived class"""

