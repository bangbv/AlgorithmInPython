

def mutate(x, y=[]):
    y.append(x)
    y = []
    return y

print(mutate(1))
print(f"mutate 2: {mutate(2)}") # Output: [], []