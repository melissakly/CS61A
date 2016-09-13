"""Optional program for lab02 """

from lab02 import *

from operator import add, sub, mul

def foldl(s, f, start):
    """Return the result of applying the function F to the initial value START
    and the first element in S, and repeatedly applying F to this result and
    the next element in S until we reach the end of the list.
    
    >>> s = [3, 2, 1]
    >>> foldl(s, sub, 0)      # sub(sub(sub(0, 3), 2), 1)
    -6
    >>> foldl(s, add, 0)      # add(add(add(0, 3), 2), 1)
    6
    >>> foldl(s, mul, 1)      # mul(mul(mul(1, 3), 2), 1)
    6

    >>> foldl([], sub, 100)   # return start if s is empty
    100
    """
    "*** YOUR CODE HERE ***"

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function CONDITION.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.
    
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
