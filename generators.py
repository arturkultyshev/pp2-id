b = (i for i in range(1, 1_000_000_000_000))
print(type(b))


def gen(n):
    for i in range(1, n):
        if i == 5:
            print('hello')
        elif i < 10:
            yield i ** 2
        else:
            break


def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


a = gen(100)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


sq = squares(3, 8)
print(next(sq))
# python -> text -> bytes -> run -> bytes -> text -> swift
