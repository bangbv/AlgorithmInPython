if __name__ == '__main__':
    X = {1, 2, 3, 4, 5}
    for x in range(X):
        print(x)

    N = int(input())
    l = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("l." + cmd)
        else:
            print(l)
