__author__ = 'changhan.ryu'

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def is_Vowel(char):
    if char in VOWELS:
        return 'v'

def is_Consonant(char):
    if char in CONSONANTS:
        return 'c'

def striped_word(word):
    count = 0
    pointer = 0
    while len(word):
        first = word[pointer]
        second = word[pointer + 1]
        pointer += 1
    if first == 'v' and second == 'c':
        count += 1

    return count