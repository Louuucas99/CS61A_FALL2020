# 1.1
"""
Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
Write a function that takes in the current temperature and a boolean value telling
if it is raining and returns True if Alfonso will wear a jacket and False otherwise
"""
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp <= 60 or raining:
        return True
    else:
        return False

"""    
Note that we’ll either return True or False based on a single condition, whose
truthiness value will also be either True or False. Knowing this, try to write this
function using a single line.
"""
def wears_jacket(temp, raining):
    return temp <= 60 or raining

#1.2 What is the result of evaluating the following code?
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0
    """
    >>> square(so_slow(5))
    infinite loop

    """
#1.3
"""
Tutorial: Write a function that returns True if a positive integer n is a prime
number and False otherwise.

A prime number n is a number that is not divisible by any numbers other than 1
and n itself. For example, 13 is prime, since it is only divisible by 1 and 13, but 14
is not, since it is divisible by 1, 2, 7, and 14.

Hint: use the % operator: x % y returns the remainder of x when divided by y.
"""
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(10)
    True
    """
    if n == 1:
        return False
    else:
        k = 2
        while k < n:
            if n % k == 0:
                return False
            k += 1
        return True























