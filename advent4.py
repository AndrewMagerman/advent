from collections import Counter

from more_itertools import pairwise


def isvalid(password: str):
    result = True

    if not len(password) == 6:
        return False

    if not single_pairf_ound(password):
        return False

    if not in_order(password):
        return False

    return single_pairf_ound(password) & in_order(password)


def countpairs(input: str):
    allpairs = dict()

    c = Counter()
    previous_char = 'X'
    for char in input:
        if char == previous_char:

            t = (previous_char, char,)
            allpairs
            c.update(t)
        previous_char = char

    return c


def single_pairf_ound(input: str):
    c = Counter()
    previous_char = 'X'
    for char in input:
        if char == previous_char:
            c.update((previous_char, char))
        previous_char = char

    print(c)
    return len(c) > 0


def in_order(input: str):
    for x, y in pairwise(input):
        if y < x:
            return False

    return True


def count_passwords():
    counter = 0
    r = Counter()
    for a in range(156218, 652527):
        password = str(a)
        if isvalid(password):
            counter += 1
            r.update([a])
            print(a)

    print(r)
    print(len(r))
    print(counter)


if __name__ == '__main__':
    # print(pairfound("hallo"))
    # print(pairfound("asadfagasdfasdf"))
    # print(in_order('145434'))
    # print(in_order('1123456'))
    # print(in_order('11923456'))
    # count_passwords()
    print(countpairs("1112233"))
