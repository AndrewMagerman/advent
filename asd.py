import itertools


def d():
    a = itertools.zip_longest([1, 2, 3, 4], [6, 7], fillvalue=0)
    e=list()
    for w in a:
        print(w)
        e.append(w)

    s = list(w for w in a)

    print(e)


if __name__ == '__main__':
    d()
