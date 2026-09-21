# ===================| Python Strings |===================

# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

print("Hello")
print('Hello')


# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# Assign String to a Variable
a = "Hello, World!"
print(a)


# Multiline Strings
# You can assign a multiline string to a variable by using three quotes(double quotes("""), single quotes(''') or combination of both):
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Note: in the result, the line breaks are inserted at the same position as in the code.


# Strings are Arrays
a = "Hello, World!"
print(a[1])  # Output: e


# Looping Through a String
for x in "banana":
    print(x)  # Output: b, a, n, a, n, a


# String Length
# To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))  # Output: 13


# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)  # Output: True
print("the" in txt)  # Output: False
print("the".capitalize() in txt)  # Output: True

# Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)  # Output: True
print("free" not in txt)  # Output: False

# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


# ===================| Python - Slicing Strings |===================

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])  # Output: llo

# Slice From the Start
# By leaving out the start index, the range will start at the first character.

# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])  # Output: Hello

# Slice To the End
# By leaving out the end index, the range will go to the end of the string.
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])  # Output: llo, World!


# Negative Indexing
# Use negative indexes to start the slice from the end of the string.
# Get the characters from position -5 to position -2 (not included).
# From the end of the string start 1st character is -1, 2nd character is -2, and so on.
b = "Hello, World!"
print(b[-5:-2])  # Output: orl


# ====================| Python - Modify Strings |===================

# Python has a set of built-in methods that you can use on strings.

# Upper Case
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())  # Output: HELLO, WORLD!


# Lower Case
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())  # Output: hello, world!


# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())  # Output: "Hello, World!"


# Replace String
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))  # Output: Jello, World!

a = "Hello, World!"
print(a.replace("World", "Universe"))  # Output: Hello, Universe!


# Split String
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))  # Output: ['Hello', ' World!']


# ===================| Python - String Concatenation |===================

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)  # Output: HelloWorld
c = a + " " + b
print(c)  # Output: Hello World


# ===================| Python - String Format |===================

# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age  # This will raise an error
print(txt) # Output: TypeError: must be str, not int (can only concatenate str (not "int") to str)

# F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)  # Output: My name is John, I am 36

# But we can combine strings and numbers by using f-strings or the format() method!
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))  # Output: For only 49.00 dollars!


# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value.
# Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)  # Output: The price is 59 dollars

# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  # Output: The price is 59.00 dollars

# A placeholder can contain Python code, like math operations:
txt = f"The price is {20 * 59} dollars"
print(txt)  # Output: The price is 1180 dollars


# ===================| Python - Escape Characters |===================

# Escape Characters
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # Output: We are the so-called "Vikings" from the north.

# Escape Characters
# Other escape characters in Python include:
"""
Code                Result
---------------------------------
\'	                Single Quote	
\"	                Double quote	
\\	                Backslash	
\n	                New Line	
\r	                Carriage Return	
\t	                Tab	
\b	                Backspace	
\f	                Form Feed	
\ooo	            Octal value	
\xhh	            Hex value
--------------------------------
"""


# ===================| Python - String Methods |===================

# String Methods
# Python has a set of built-in methods that you can use on strings.

# Note: All string methods return new values. They do not change the original string.

'''
Method               Description
---------------------------------------------------------------------------------------------
title()              Converts the first character of each word to upper case
upper()              Converts a string into upper case
lower()              Converts a string into lower case
swapcase()           Swaps cases, lower case becomes upper case and vice versa
capitalize()         Converts the first character to upper case
casefold()           Converts string into lower case
center()             Returns a centered string
count()              Returns the number of times a specified value occurs in a string
encode()             Returns an encoded version of the string
endswith()           Returns true if the string ends with the specified value
expandtabs()         Sets the tab size of the string
find()               Searches the string for a specified value and returns the position of where it was found
format()             Formats specified values in a string
format_map()         Formats specified values in a string
index()              Searches the string for a specified value and returns the position of where it was found
isalnum()            Returns True if all characters in the string are alphanumeric
isalpha()            Returns True if all characters in the string are in the alphabet
isascii()            Returns True if all characters in the string are ascii characters
isdecimal()          Returns True if all characters in the string are decimals
isdigit()            Returns True if all characters in the string are digits
isidentifier()       Returns True if the string is an identifier
islower()            Returns True if all characters in the string are lower case
isnumeric()          Returns True if all characters in the string are numeric
isprintable()        Returns True if all characters in the string are printable
isspace()            Returns True if all characters in the string are whitespaces
istitle()            Returns True if the string follows the rules of a title
isupper()            Returns True if all characters in the string are upper case
join()               Joins the elements of an iterable to the end of the string
ljust()              Returns a left justified version of the string
lstrip()             Returns a left trim version of the string
maketrans()          Returns a translation table to be used in translations
partition()          Returns a tuple where the string is parted into three parts
replace()            Returns a string where a specified value is replaced with a specified value
rfind()              Searches the string for a specified value and returns the last position of where it was found
rindex()             Searches the string for a specified value and returns the last position of where it was found
rjust()              Returns a right justified version of the string
rpartition()         Returns a tuple where the string is parted into three parts
rsplit()             Splits the string at the specified separator, and returns a list
rstrip()             Returns a right trim version of the string
split()              Splits the string at the specified separator, and returns a list
splitlines()         Splits the string at line breaks and returns a list
startswith()         Returns true if the string starts with the specified value
strip()              Returns a trimmed version of the string
translate()          Returns a translated string
zfill()              Fills the string with a specified number of 0 values at the beginning
----------------------------------------------------------------------------------------------
'''

