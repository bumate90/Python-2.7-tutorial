import math


def primeNumbers(threshold):
    for i in range(1, threshold + 1):
        c = 0
        for j in range(2, int(math.sqrt(i)) + 1):
            if (i % j) == 0:
                c += 1
        if c == 0:
            print i


def removeStrDuplicates(string):
    result = ''
    my_dict = {}
    for c in string:
        if not my_dict.has_key(c):
            my_dict[c] = True
            result += c
    return result


print removeStrDuplicates("abcadaaaaeeefg")
