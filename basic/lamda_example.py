# syntax
# lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

# The power of lambda is better shown
# when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n

my_doubler = myfunc(2)
my_tripler = myfunc(3)

print(my_doubler(11))
print(my_tripler(11))