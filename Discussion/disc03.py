#1.1
def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m,n-1)
            
#1.3
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
number of elements in the sequence
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
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1+hailstone(n//2)
    else:
        return 1+hailstone(n * 3 + 1)

#1.4
def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10
        
#1.5
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(y):
        if y == 1:
            return f(x)
        else:
            return f(repeat(y-1))
    return repeat

#1.6
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(index):
        if index == n:
            return True
        elif n % index == 0 or n ==1:
            return False
        else:
            return prime_helper(index+1)
    return prime_helper(2)
    
