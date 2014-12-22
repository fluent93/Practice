__author__ = 'changhan.ryu'

def secure_pwd(str) :
    count_digit = 0
    count_lower = 0
    count_upper = 0

    if len(str) < 10:
        return False
    else:
        for i in str:
            if i.isdigit():
                count_digit += 1
            if i.islower():
                count_lower += 1
            if i.isupper():
                count_upper += 1

        if count_upper >=1 and count_lower >=1 and count_digit >=1:
            return True
        return False