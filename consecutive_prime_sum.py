__author__ = 'changhanryu'

from prime_number import isPrime

def prime_lst(n):
    lst = [x for x in range(3, n, 2) if isPrime(x)]
    lst.insert(0,2)
    return lst


def subsum(lst, n):
    count = 0
    total = 0
    temp = 0
    for i in range(len(lst)):
        temp += lst[i]
        if temp > n:
            break
        if temp in lst:
            total = temp
            count = i + 1
    return [count, total]

def max_sum(lst, n):
    temp_lst = []
    for i in range(len(lst)):
        temp_lst.append(subsum(lst[i:], n))

    return max(temp_lst)