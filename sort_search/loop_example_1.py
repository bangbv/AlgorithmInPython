# Two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

def my_transform(x):
    return f"{x}_new"

# Using for and zip to iterate through both lists
print("Name and Score Pairs:")
output = [my_transform(name) for name, score in zip(names, scores)]
print(f"output: {output}")
