#DISC 04
#1.1
"""
Q:   You want to go up a flight of stairs that has n steps. You can either take 1
or 2 steps each time. How many different ways can you go up this flight of
stairs? Write a function count_stair_ways that solves this problem. Assume
n is positive.
A:   When there is only 1 step, there is only one way to go up the stair. When
there are two steps, we can go up in two ways: take a two-step, or take 2
one-steps.
Q: Before we start, what’s the base case for this question? What is the simplest
input?
A:   Our first base case is where there are no steps left. This means that we took
an action in the previous recursive step that led to our goal of reaching the
top. Our second base case is where we have overstepped. This means that
the action we took is not valid, as it caused us to step over our goal.
Q:   What do count_stair_ways(n - 1) and count_stair_ways(n - 2) represent?
A:    count_stair_ways(n - 1) represents the number of different ways to go up
the last n − 1 stairs (this is the case where we take 1 step as our move).
count_stair_ways(n - 2) represents the number of different ways to go up
the last n−2 stairs (this is the case where we take 2 steps as our move). Our
base cases will take care of if there are no steps left or if we overstepped.
"""
def count_stair_ways(n):
    assert n >= 0, "can't go down stairs"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)


#1.2
"""
Tutorial: Consider a special version of the count_stairways problem,
where instead of taking 1 or 2 steps, we are able to take up to and including
k steps at a time.
Write a function count_k that figures out the number of paths for this scenario.
Assume n and k are positive.
"""
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total
