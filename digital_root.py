__author__ = 'changhanryu'

"""
A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
Here's how it works:

digital_root(16) ...
=> 1 + 6
=> 7
"""

def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(map(int, str(n))))