__author__ = 'changhan.ryu'

def is_selfNumber (n):
    j = 1
    s = str(j)
    temp = 0
    while j < n:
        for i in s:
            temp += int(i)
        if (temp + j) == n:
            return False

    return True
