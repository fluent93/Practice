__author__ = 'changhan.ryu'

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True