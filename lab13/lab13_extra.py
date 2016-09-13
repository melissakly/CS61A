## Optional Questions ##

# Naturals generator

def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

# Q4

def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"

class Countdown:
    """
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    def __init__(self, cur):
        self.cur = cur

    def __iter__(self):
        "*** YOUR CODE HERE ***"

# Q5

def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"

# Q6

def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. You can also assume that s0
    and s1 represent infinite sequences.

    >>> twos = scale(naturals(), 2)
    >>> threes = scale(naturals(), 3)
    >>> m = merge(twos, threes)
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0), next(i1)
    "*** YOUR CODE HERE ***"

# Q7 and 8

def pairs(lst):
    """
    >>> type(pairs([3, 4, 5]))
    <class 'generator'>
    >>> for x, y in pairs([3, 4, 5]):
    ...     print(x, y)
    ...
    3 3
    3 4
    3 5
    4 3
    4 4
    4 5
    5 3
    5 4
    5 5
    """
    "*** YOUR CODE HERE ***"

class PairsIterator:
    """
    >>> for x, y in PairsIterator([3, 4, 5]):
    ...     print(x, y)
    ...
    3 3
    3 4
    3 5
    4 3
    4 4
    4 5
    5 3
    5 4
    5 5
    """
    def __init__(self, lst):
        "*** YOUR CODE HERE ***"

    def __next__(self):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        "*** YOUR CODE HERE ***"

# Q9

def remainders_generator(m):
    """
    Takes in an integer m, and yields m different remainder groups
    of m.

    >>> remainders_mod_four = remainders_generator(4)
    >>> for rem_group in remainders_mod_four:
    ...     for _ in range(3):
    ...         print(next(rem_group))
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"

# Q10

def supplier(ingredients, chef):
    for ingredient in ingredients:
        try:
            chef.send(ingredient)
        except StopIteration as e:
            print(e)
            break
    chef.close()
def customer():
    served = False
    while True:
        try:
            dish = yield
            print('Yum! Customer got a {}!'.format(dish))
            served = True
        except GeneratorExit:
            if not served:
                print('Customer never got served.')
            raise
def chef(customers, dishes):
    """
    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun', 'hotdog'], c)
    Yum! Customer got a hotdog!
    Chef went home.

    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun'], c)
    Chef went home.
    Customer never got served.

    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun', 'hotdog', 'mustard'], c)
    Yum! Customer got a hotdog!
    No one left to serve!
    """
    "*** YOUR CODE HERE ***"
