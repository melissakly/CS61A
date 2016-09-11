
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n==1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone((n*3)+1)

def symmetric(l):
    """Returns whether a list is symmetric. 
    >>> symmetric([])
    True
    >>> symmetric([1])
    True
    >>> symmetric([1, 4, 5, 1])
    False
    >>> symmetric([1, 4, 4, 1])
    True
    >>> symmetric(['l', 'o', 'l'])
    True
    """
    if len(l) < 2:
        return True
    elif l[0] == l[-1]:
        return symmetric(l[1:-1])
    else:
        return False
