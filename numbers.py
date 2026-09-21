# ===================| Python Numbers |===================

# Python has three numeric types: 
# int
# float
# complex

# Variables of numeric types are created when you assign a value to them:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(x, type(x))
print(y, type(y)) 
print(z, type(z))


# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(x, type(x))
print(y, type(y)) 
print(z, type(z))

# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59

print(x, type(x))
print(y, type(y)) 
print(z, type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100

print(x, type(x))
print(y, type(y)) 
print(z, type(z))


# Complex
# Complex numbers are written with a "j" as the imaginary part:
x = 3 + 5j
y = 5j
# z = -5j
z = 0-5j

print(x, type(x))
print(y, type(y)) 
print(z, type(z))

# ===================| Type Conversion |===================

# You can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Note: You cannot convert complex numbers into another number type.


# ===================| Random Number |===================
# Python has a built-in module called random that can be used to make random numbers:
# Import the random module, and display a random number from 1 to 9:
import random

print(random.randrange(1, 10))


# Binary, Octal, and Hexadecimal Literals
# In Python, you can represent numbers in different numeral systems. Here are the literals for binary, octal, and hexadecimal:

# Binary literals are prefixed with '0b' or '0B':
binary_number = 0b1010  # This represents the binary number for 10 in decimal
print(binary_number)  # Output: 10

# Octal literals are prefixed with '0o' or '0O':
octal_number = 0o12  # This represents the octal number for 10 in decimal
print(octal_number)   # Output: 10

# Hexadecimal literals are prefixed with '0x' or '0X':
hexadecimal_number = 0xA  # This represents the hexadecimal number for 10 in decimal
print(hexadecimal_number)  # Output: 10


# ===================| Python Built-in Functions |===================
# Python provides many built-in functions that can be used directly
# Without importing any module. Here are some of the most commonly used built-in functions for numbers:

# Number MethodsFunctions Related to Numbers
'''
Function               Description
---------------------------------------------------
abs()                  Absolute value
bin()                  Convert number → binary
hex()                  Convert number → hexadecimal
oct()                  Convert number → octal
pow()                  Power calculation
round()                Round number
divmod()               Returns quotient and remainder
complex()              Creates complex number
float()                Convert to float
int()                  Convert to integer
sum()                  Sum of iterable
max()                  Maximum value
min()                  Minimum value
---------------------------------------------------
'''

print(0b1010)  # 10
print(0o12)    # 10
print(0x10)    # 16

print(bin(10))      # 0b1010
print(hex(10))      # 0xa
print(oct(10))      # 0o12

num = -10

print(abs(num))     # 10
print(pow(2, 3))    # 8
print(round(5.67))  # 6
print(divmod(10, 3))  # (3, 1)
print(complex(2, 3))  # (2+3j)
print(float(10))    # 10.0
print(int(10.5))    # 10
print(sum([1, 2, 3]))  # 6
print(max(1, 2, 3))  # 3
print(min(1, 2, 3))  # 1

# ===================| ASCII and Unicode |===================
# Python uses Unicode to represent characters.
# Each character is assigned a unique code point, which can be represented in different ways, such as ASCII or Unicode.

# Unicode
print("\u0041")  # A
print("\u005A")  # Z
print("\u0061")  # a
print("\u007A")  # z
print("\u0030")  # 0
print("\u0031")  # 1

print("\\u{:04X}".format(ord('A'))) # \u0041
print("\\u{:04X}".format(ord('Z'))) # \u005A
print("\\u{:04X}".format(ord('a'))) # \u0061
print("\\u{:04X}".format(ord('z'))) # \u007A
print("\\u{:04X}".format(ord('0'))) # \u0030
print("\\u{:04X}".format(ord('1'))) # \u0031


# Simple Rule
# ord(character) → ASCII value
# chr(number) → Character
# ASCII
print(chr(48)) # 0
print(chr(49)) # 1
print(chr(65)) # A
print(chr(90)) # Z
print(chr(97)) # a
print(chr(122)) # z

print(ord('0')) # 48
print(ord('1')) # 49
print(ord('A')) # 65
print(ord('Z')) # 90
print(ord('a')) # 97
print(ord('z')) # 122


a = "\u0030" #unicode for 0
b = "\u0041" #unicode for A

print(a) # 0
print(b) # A
print(a.isdecimal()) # True
print(a.isdigit())   # True
print(a.isnumeric()) # True
print(a.isascii())   # True
print(b.isascii())   # True
print(a.isalpha())   # False
print(b.isalpha())   # True


# ===================| Number Systems |===================

# In Binary, the numbers 2 to 9 are not used. Instead, binary uses only the digits 0 and 1.
# 0, 1

# In Octal, the numbers 8 and 9 are not used. Instead, octal uses only the digits 0 to 7.
# 0, 1, 2, 3, 4, 5, 6, 7

# In the Decimal system, we use the digits 0 to 9 to represent numbers.
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# In Hexadecimal, the numbers 10 to 15 are represented by the letters A to F
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F


# Practice Exercise: Convert the number 360 into binary, octal, and hexadecimal formats using the built-in functions.
print("----------------| Practice Exercise |----------------")

n = 360 # Decimal representation
print(bin(n)) # Binary representation
print(oct(n)) # Octal representation
print(hex(n)) # Hexadecimal representation

x = 0xACE # 2766 in decimal
x = 0xBAD # 2989 in decimal
x = 0xBE # 190 in decimal
x = 0xBEE # 3054 in decimal
x = 0xBEEF # 48879 in decimal
x = 0xBED # 3053 in decimal
x = 0xCAB # 3243 in decimal
x = 0xCAFE # 51966 in decimal
x = 0xDEAF # 57007 in decimal
x = 0xDEFACE # 14613198 in decimal
x = 0xFACE # 64206 in decimal 
x = 0xFACED # 1023213 in decimal
x = 0xFADE # 64222 in decimal
x = 0xFEED # 65261 in decimal
x = 0xDEAD # 57005 in decimal
print(x)


# Famous Hex Words
# Hex Value	Meaning / Usage
# 0xDEADBEEF	Very famous debugging value (used to mark freed memory)
# 0xCAFEBABE	Magic number in Java .class files
# 0xBEEF	    Debugging marker
# 0xFACE	    Fun readable hex value
# 0xFEEDFACE	Used in Mach-O binaries (macOS executable format)
# 0xDEAD	    Often used for terminated processes or errors
# 0xFADE	    Example hex word
# 0xCAFE	    Used in many programming examples
# 0xDEFACE	    Another readable hex pattern
# 0xDEAF	    Hex word
# 0xBABE	    Simple hex word
# 0xBADA55	    “badass” (leet-style hexspeak)