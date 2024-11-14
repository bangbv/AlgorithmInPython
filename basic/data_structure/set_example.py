# A set is an unordered collection with no duplicate elements.
# Curly braces or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {};
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(f"basket set: {basket}")


# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(f"a set: {a}")
print(f"b set: {b}")
# letters in A but not in B
print(f"a - b set: {a-b}")
# letters in a or b or both
print(f"a | b set: {a|b}")
# letters in both a and b
print(f"a & b set: {a&b}")
# letters in a or b but not both
print(f"a ^ b set: {a^b}")