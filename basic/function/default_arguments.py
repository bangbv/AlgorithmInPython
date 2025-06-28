
def greet(greeting="Hello", name="Guest"):
    """
    Greets a person with a default name and greeting.

    :param name: The name of the person to greet. Defaults to "Guest".
    :param greeting: The greeting message. Defaults to "Hello".
    """
    return f"{greeting}, {name}!"

if __name__ == "__main__":
    print(greet())
    print(greet("Hi", "Bang"))