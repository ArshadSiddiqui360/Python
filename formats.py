# ===================| String Formatting |===================

# Python String format() Method
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
# The format() method returns the formatted string.

# Syntax
# string.format(value1, value2...)

# Parameter Values
'''
value1, value2, ...     These are the values that will be formatted and inserted in the string. The format() method takes unlimited number of parameters.
                        The values are either a list of values separated by commas, a key=value list, or a combination of both.
                        The values can be of any data type.
'''

# The Placeholders
# The placeholders can be identified using named indexes {name}, numbered indexes {0}, or even empty placeholders {}.

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print(txt1) # Output: My name is John, I'm 36

txt2 = "My name is {0}, I'm {1}".format("John",36)
print(txt2) # Output: My name is John, I'm 36

txt3 = "My name is {}, I'm {}".format("John",36)
print(txt3) # Output: My name is John, I'm 36

txt = "The Hexadecimal version of {0} is {0:.2%}"
print(txt.format(450/500)) # Output: The Hexadecimal version of 0.9 is 90.00%


# ===================| Formatting Types |===================
'''
# Inside the placeholders you can add a formatting type to format the result:
-------------------------------------------------------------------------------------
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format
-------------------------------------------------------------------------------------
'''