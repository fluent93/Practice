__author__ = 'changhanryu'


def is_selfNumber(n):
    origin_number = 0
    digit_sum = 0
    total_sum = 0
    while origin_number < n:
        s = str(origin_number)
        for i in s:
            digit_sum += int(i)
        total_sum = origin_number + digit_sum
        if total_sum == n:
            return False
        origin_number += 1
        digit_sum = 0
    return True

def sum_of_selfNumber(n):
    lst = [x for x in range(n) if is_selfNumber(x)]
    return sum(lst)