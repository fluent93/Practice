__author__ = 'changhan.ryu'

#find the largest prime factor from Euler

def largest_prime_factor(n):
    divisor = 2
# When the number is equal to the divisor, it returns the largest prime factor
    while n != divisor:
# Keep reduce the number 'n' dividing by divisor
        while n % divisor == 0:
            n /= divisor
 # When the current divisor(current prime factor) is not able to divide the number 'n',
# divisor is increased by 1 up until it is equal to the number 'n'
        divisor += 1
    return divisor


def prime_factors(n):
    divisor = 2
    prime_factors_lst = []
    while n != divisor:
        while n % divisor == 0:
            prime_factors_lst.append(divisor)
            n /= divisor
        divisor += 1
 # add the last(largest) prime factor to the list
    prime_factors_lst.append(divisor)
 # Use the set() function in order to the remove the duplicate element in the list.
# (ex. n = 20, we have two '2' prime factors)
# Finally add 'list' to make this set back to the list. from {} to []
    return list(set(prime_factors_lst))