__author__ = 'changhanryu'


def SN_sum():
    S = sum(range(5000))
    GN = sum([digit_sum(i) for i in range(5000) if digit_sum(i) < 5000])
    return S - GN

def digit_sum(n):
    s = str(n)
    total = 0
    for i in s:
        total += int(i)
    return total + n