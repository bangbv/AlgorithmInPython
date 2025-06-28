

def outer(x):
    def inner(y):
        return x + y
    return inner

if __name__ == "__main__":
    add_five = outer(5)
    result = add_five(10)
    print(f"Result of adding 5 and 10: {result}")  # Should print 15