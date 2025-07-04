text = "        Hello, World!   "
print(f"My content:{text}") # Original text with leading and trailing whitespace
print(f"My content:{text.strip()}") # Remove leading and trailing whitespace
print(f"My content:{text.replace('World', 'Python')}") # Replace "World" with "Python"
print(f"My content:{text.split(',')}") # Split the string by comma