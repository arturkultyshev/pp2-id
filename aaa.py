def gen(n):
    a = (i for i in range(1, 1000001))
    if n in a:
        yield True
    else:
        yield False

print(next(gen(2000)))
print(next(gen(2000)))