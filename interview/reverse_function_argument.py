# https://stackoverflow.com/questions/9850259/flipping-a-functions-argument-order-in-python

def f(a, b):
    return a ** b


def transform(f):
    return lambda *args: f(*args[::-1])


if __name__ == '__main__':
    g = transform(f)
    print(g(4, 5))
