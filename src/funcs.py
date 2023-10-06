from math import sqrt
"""Exercises with simple functions"""


def prod(a, b, c):
    return a * b * c
    """
    Compute the product of three numbers.

    >>> prod(1, 2, 3)
    6
    """
    ...


a = 2
def prod2(b):
    c = 5
    return a * b * c
    """
    Get a global a and write to a local c before computing prod(a, b, c)

    >>> prod2(42)
    420
    """
    ...


def longest(x, y):
    if len(x) > len(y):
        return x
    else:
        return y
    """
    Returning the longest of two lists.

    >>> longest([1, 2, 3], [4, 5])
    [1, 2, 3]
    """
    ...


def dist(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    """
    Compute the distance between p1 and p2.

    >>> dist((1,2), (3,4))
    8 ** 0.5
    """
    x1, y1 = p1
    x2, y2 = p2
    ...
