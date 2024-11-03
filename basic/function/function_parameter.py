def apply_function(f, value):
    return f(value)

def square(x):
    return x * x

result = apply_function(square, 5)
print(result)  # Output: 25
