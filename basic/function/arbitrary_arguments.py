"Arbitrary Arguments, *args"
"If you do not know how many arguments that will be passed into your function, \
add a * before the parameter name in the function definition."

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


"Arbitrary Keyword Arguments, **kwargs"
""" 
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.\
"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")