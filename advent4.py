from collections import Counter

from more_itertools import pairwise


def is_valid_part1(password: str):
    if not len(password) == 6:
        return False

    if not in_order(password):
        return False

    return pair_found(password)


def is_valid_part2(password: str):
    if not len(password) == 6:
        return False

    if not in_order(password):
        return False

    return at_least_one_pure_pair(password)


def at_least_one_pure_pair(password: str):
    a = pair_counter(password)
    return 1 in a.values()


def pair_found(password: str):
    a = pair_counter(password)
    return len(a) > 0


def in_order(password: str):
    for x, y in pairwise(password):
        if y < x:
            return False
    return True


def pair_counter(password: str):
    counter = Counter()
    for pair in pairwise(password):
        x, y = pair
        if x == y:
            counter[pair] += 1
    return counter


def count_passwords(func):
    counter = 0

    for a in range(156218, 652527):
        password = str(a)
        if func(password):
            counter += 1

    return counter


if __name__ == '__main__':
    print(count_passwords(is_valid_part1))
    print(count_passwords(is_valid_part2))

    # 1694
    # 1148
