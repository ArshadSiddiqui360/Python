# ===================| Python Casting |===================

# There may be times when you want to specify a type on to a variable. This can be done with casting.
# There are several built-in functions to perform conversion from one data type to another.

# Specify a Variable Type - Casting in python is therefore done using constructor functions:
# int() - constructs an integer number from an integer literal, a float literal (by rounding down to the nearest whole number), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal, or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integers and floats

# Integers:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# Strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'