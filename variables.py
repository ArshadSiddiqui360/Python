# ===================| Python Variables |===================

# Creating Variables
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type, 
# Change type after they have been set.
x = 4       # x is of type int
x = "John"  # x is now of type str
print(x)

# Casting
x = str(5)    # x will be '5'
y = int(5)    # y will be 5
z = float(5)  # z will be 5.0

# Get the Value & Type
print(x, type(x))
print(y, type(y))
print(z, type(z))

# Single or Double Quotes
a = "Hello"
# is the same as
a = 'Hello'

# Case-Sensitive
# Variable names are case-sensitive.
a = 4
A = "John"
# A will not overwrite and both variables will exist, but with different values
print(a)
print(A)

# ===================| Python - Variable Names |===================
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Multi Words Variable Names

# Camel Case - Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case - Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case - Each word is separated by an underscore character:
my_variable_name = "John"


# ===================| Python - Assign Multiple Values |===================

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# ===================| Python - Output Variables |===================

# The print() function is often used to output variables.
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
x = "Python"
y = "is"
z = "awesome"
print(x + y + z)
print(x + " " + y + " " + z)


# ===================| Python - Global Variables |===================
# Global variables are variables that are created outside of a function and can be used anywhere in the code.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# The global Keyword
# If you use the global keyword, the variable belongs to the global scope:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)