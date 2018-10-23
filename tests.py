def simple(x):
    print(x)
    y = yield x * 2
    print(y)
    z = yield y + x
    print(z)

s = simple(2)
next(s)
print(s.send(3))