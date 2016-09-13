"""Lab 1."""

# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    while n>0:
        n-=1
        x=f(x)
    return x

# If Statements

def xk(c, d):
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25

def how_big(x):
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print("nothin'")

def so_big(x):
    if x > 10:
        print('huge')
    if x > 5:
        return 'big'
    if x > 0:
        print('small')
    print("nothin'")

# Boolean Operators

def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x and y > 0 # You can replace this line!

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"

# Lists

def factors_list(n):
    """Return a list containing all the numbers that divide `n`
    evenly, except for the number itself. Make sure the list is in
    ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    x = 1
    while x < n:
        if n % x == 0:
            all_factors += [x]
        x += 1
    return all_factors

def perfect_number(n):
    """Returns True or False indicating whether `n` is a perfect 
    number. A number is a perfect number when the sum of all its 
    factors equal the number itself.

    >>> perfect_number(6)
    True
    >>> perfect_number(8)
    False
    >>> perfect_number(28)
    True
    """
    all_factors = factors_list(n)
    "*** YOUR CODE HERE ***"

# Guessing Game

from random import randint

LOWER = 1
UPPER = 10

def guess_random():
    """Guess randomly and return the number of guesses."""
    prompt_for_number(LOWER, UPPER)   # asks the user to choose a number
    num_guesses, correct = 0, False
    while not correct:
        guess = randint(LOWER, UPPER) # randomly guess
        correct = is_correct(guess)   # ask user if guess is correct
        num_guesses = num_guesses + 1
    return num_guesses

def guess_linear():
    """Guess in increasing order and return the number of guesses."""
    prompt_for_number(LOWER, UPPER)
    num_guesses = 1
    guess = LOWER
    "*** YOUR CODE HERE ***"
    return num_guesses

def guess_binary():
    """Return the number of attempted guesses. Implement a faster search
    algorithm that asks the user whether a guess is less than or greater than
    the correct number.

    Hint: If you know the guess is greater than the correct number, then your
    algorithm doesn't need to try numbers that are greater than guess.
    """
    prompt_for_number(LOWER, UPPER)
    num_guesses = 1
    lower, upper = LOWER, UPPER
    guess = (lower + upper) // 2
    "*** YOUR CODE HERE ***"
    return num_guesses

# Receive user input. You do not need to understand the code below this line.

def prompt_for_number(lower, upper):
    """Prompt the user for a number between lower and upper. Return None."""
    is_valid_number = False
    while not is_valid_number:
        # You don't need to understand the following two lines.
        number = input('Pick an integer between {0} and {1} (inclusive) for me to guess: '.format(lower, upper))
        number = int(number)
        if lower <= number <= upper:
            is_valid_number = True

def is_correct(guess):
    """Ask the user if a guess is correct and return whether they respond y."""
    return is_yes('Is {0} your number? [y/n] '.format(guess))

def is_too_high(guess):
    """Ask the user if a guess is too high and return whether they say yes."""
    return is_yes('Is {0} too high? [y/n] '.format(guess))

def is_yes(prompt):
    """Ask the user a yes or no question and return whether they say yes."""
    while True: # This while statement will loop until a "return" is reached.
        yes_no = input(prompt).strip()
        if yes_no == 'y':
            return True
        elif yes_no == 'n':
            return False
        print('Please type y or n and press return/enter')