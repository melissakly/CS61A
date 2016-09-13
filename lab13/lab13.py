## Lab 13: Coroutines ##

# Q3

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    num = n 
    while num != 1:
        if num%2 == 0:
            yield num
            num = num // 2
        else:
            yield num
            num = (num * 3) + 1
    print (1) 

