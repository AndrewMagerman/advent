from collections import Counter

from more_itertools import pairwise


def isvalid(password: str):
    result = True

    if not len(password) == 6:
        return False

    if not pair_found(password):
        return False

    if not in_order(password):
        return False

    return pair_found(password) & in_order(password) & at_least_one_pure_pair(password)


def at_least_one_pure_pair(input: str):
    c = countpairs(input)
    for value in c.values():
        if value == 1:
            return True

    return False


def countpairs(input: str):
    allpairs = dict()

    c = Counter()
    previous_char = 'X'
    for char in input:
        if char == previous_char:
            t = (previous_char, char,)
            if t not in allpairs:
                allpairs[t] = 1
            else:
                allpairs[t] += 1
            c.update(t)
        previous_char = char

    print(c)
    print(allpairs)
    return allpairs


def pair_found(input: str):
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


def pair_counter(input: str):
    e = Counter()
    for a in pairwise(input):
        x, y = a
        if x == y:
            e[a] += 1
    return e


def count_passwords():
    counter = 0

    for a in range(156218, 652527):
        password = str(a)
        if isvalid(password):
            counter += 1

    return counter


if __name__ == '__main__':
    # print(pairfound("hallo"))
    # print(pairfound("asadfagasdfasdf"))
    # print(in_order('145434'))
    print(pair_counter('1123456'))
    # print(in_order('11923456'))
    # count_passwords()
    # print(countpairs("1112233"))
    # print(at_least_one_pure_pair("1122222"))
