if __name__ == '__main__':
    n = 7
    arr = [1, 2, 3, 6, 6, 6, 5, 4]
    la = list(arr)
    m = max(la)
    while max(la) == m:
        la.remove(m)
    print(max(la))
