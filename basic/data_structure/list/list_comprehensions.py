# List comprehensions provide a concise way to create lists.
# Common applications are to make new lists where each element is the result of some operations
# applied to each member of another sequence or iterable,
# or to create a subsequence of those elements that satisfy a certain condition.
if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3
    result = [
        [a, b, c]
        for a in range(0, x + 1)
        for b in range(0, y + 1)
        for c in range(0, z + 1)
        if a + b + c != n]
    print(result)
