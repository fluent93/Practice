__author__ = 'changhanryu'


def SN_sum():
    S = sum(range(5000))
    GN = sum(set([digit_sum(i) for i in range(5000) if digit_sum(i) < 5000]))
    return S - GN

def digit_sum(n):
    return n + sum([int(x) for x in str(n)])