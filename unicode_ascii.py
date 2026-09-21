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