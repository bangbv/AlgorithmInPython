def process_numbers(numbers, operation):
    """
    Applies the given operation to each number in the list.

    Parameters:
    numbers (list): A list of numbers.
    operation (function): A function that takes a number and returns a number.

    Returns:
    list: A list of results after applying the operation.
    """
    return [operation(number) for number in numbers]


# Define some operations
def double(x):
    return x * 2


def triple(x):
    return x * 3


def square(x):
    return x ** 2


# Usage
nums = [1, 2, 3, 4, 5]

doubled = process_numbers(nums, double)
tripled = process_numbers(nums, triple)
squared = process_numbers(nums, square)

print("Original:", nums)
print("Doubled:", doubled)
print("Tripled:", tripled)
print("Squared:", squared)
