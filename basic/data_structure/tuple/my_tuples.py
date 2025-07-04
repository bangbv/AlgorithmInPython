# A tuple consists of a number of values separated by commas
if __name__ == '__main__':
    t = 12345, 54321, 'hello!'
    print(f"t tuple: {t}")
    print(f"t[0]: {t[0]}")

    # Tuples may be nested:
    u = t, (1, 2, 3, 4, 5)
    print(f"u tuple: {u}")
