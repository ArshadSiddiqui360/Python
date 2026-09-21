# ===================| Python Operators |===================
print('-------------------| Python Operators |-------------------')

# Operators are used to perform operations on variables and values.

# In the example below, we use the + operator to add together two values:
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print(sum3)

# Python divides the operators in the following groups:
"""
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""


# ===================| Python - Arithmetic Operators |===================
print('-------------------| Python - Arithmetic Operators |-------------------')

# Arithmetic operators are used with numeric values to perform common mathematical operations

"""
Operator    Name                Result
----------------------------------------
+	        Addition	        x + y	
-	        Subtraction	        x - y	
*	        Multiplication	    x * y	
/	        Division	        x / y	
%	        Modulus	            x % y	
**	        Exponentiation	    x ** y	
//	        Floor division	    x // y
----------------------------------------
"""

# Here is an example using different arithmetic operators:
x = 15
y = 4

print(x + y) # 19
print(x - y) # 11
print(x * y) # 60
print(x / y) # 3.75
print(x % y) # 3
print(x ** y) # 50625
print(x // y) # 3


# ===================| Python - Assignment Operators |===================
print('-------------------| Python - Assignment Operators |-------------------')

# Assignment operators are used to assign values to variables.

"""
Operator    Example             Same As
----------------------------------------
=	        x = 5	            x = 5	
+=	        x += 3	            x = x + 3	
-=	        x -= 3	            x = x - 3	
*=	        x *= 3	            x = x * 3	
/=	        x /= 3	            x = x / 3	
%=	        x %= 3	            x = x % 3	
//=	        x //= 3	            x = x // 3	
**=	        x **= 3	            x = x ** 3	
&=	        x &= 3	            x = x & 3	
|=	        x |= 3	            x = x | 3	
^=	        x ^= 3	            x = x ^ 3	
>>=	        x >>= 3	            x = x >> 3	
<<=	        x <<= 3	            x = x << 3	
:=	        print(x := 3)	    x = 3
                                print(x)
----------------------------------------
"""


# The Walrus Operator
# Python 3.8 introduced the := operator, known as the "walrus operator".
# It assigns values to variables as part of a larger expression.

# The count variable is assigned in the if statement, and given the value 5
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Same as
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

# OR
count = len(numbers)
if (count > 3):
    print(f"List has {count} elements")


# ===================| Python - Comparison Operators |===================
print('-------------------| Python - Comparison Operators |-------------------')

# Comparison operators are used to compare two values

"""
Operator    Name                        Example
------------------------------------------------
==	        Equal	                    x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y	
------------------------------------------------
"""

x = 5
y = 5
z = 10

print(x == y) # True
print(x != y) # False
print(x > z) # False
print(y < z) # True
print(x >= z) # False
print(y <= z) # True


# ===================| Python - Logical Operators |===================
print('-------------------| Python - Logical Operators |-------------------')

# Logical operators are used to combine conditional statements
"""
Operator    Description                                                 Example
---------------------------------------------------------------------------------------------
and 	    Returns True if both statements are true	                x < 5 and  x < 10	
or	        Returns True if one of the statements is true	            x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)
---------------------------------------------------------------------------------------------
"""

# Test if a number is greater than 0 and less than 10:
x = 5
print(x > 0 and x < 10) # True

# Test if a number is less than 5 or greater than 10:
x = 5
print(x < 5 or x > 10) # False

# Reverse the result with not:
x = 5
print(not(x > 3 and x < 10)) # False


# ===================| Python - Identity Operators |===================
print('-------------------| Python - Identity Operators |-------------------')

# Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location.
"""
Operator    Description                                                 Example
------------------------------------------------------------------------------------
is 	        Returns True if both variables are the same object	        x is y	
is not	    Returns True if both variables are not the same object	    x is not y
------------------------------------------------------------------------------------
"""

# The is operator returns True if both variables point to the same object:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # True
print(x is y) # False
print(x == y) # True


# The is not operator returns True if both variables do not point to the same object:
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y) # True


# Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) # True
print(x is y) # False

# ===================| Python - Membership Operators |===================
print('-------------------| Python - Membership Operators |-------------------')

# Membership operators are used to test if a sequence is presented in an object (Case sensitive)

"""
Operator    Description                                                                         Example
----------------------------------------------------------------------------------------------------------
in 	        Returns True if a sequence with the specified value is present in the object	    x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y
----------------------------------------------------------------------------------------------------------
"""

# Check if "banana" is present in a list:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # True
print("Banana" in fruits) # False (Case sensitive)

# Check if "pineapple" is NOT present in a list:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits) # True


# Membership in Strings
# The membership operators also work with strings:
text = "Hello World"
print("H" in text) # True
print("hello" in text) # False
print("z" not in text) # True


# ===================| Python - Bitwise Operators |===================
print('-------------------| Python - Bitwise Operators |-------------------')

# Bitwise operators are used to compare (binary) numbers
"""
Note: 
1. Bits and Bytes Basics
    1 byte = 8 bits
    A bit can be 0 or 1

2. Decimal → Binary (Bits)
    Decimal 2 in binary is:
    2 → 10
    So:
        2 = 2 bits minimum (10)
        In 1 byte (8 bits):
        00000010
"""

"""
Operator	Name	                Description	                                                                                                Example
-------------------------------------------------------------------------------------------------------------------------------------------------------
& 	        AND	                    Sets each bit to 1 if both bits are 1	                                                                    x & y	
|	        OR	                    Sets each bit to 1 if one of two bits is 1	                                                                x | y	
^	        XOR	                    Sets each bit to 1 if only one of two bits is 1	                                                            x ^ y	
~	        NOT	                    Inverts all the bits	                                                                                    ~x	
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                        x << 2	
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off     x >> 2

^	        XNOR	                Sets each bit to 1 if both of two bits are same, 0 when different (Mask when working with multiple bits)    ~(x ^ y)
-------------------------------------------------------------------------------------------------------------------------------------------------------
"""

# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
print(6 & 3) # 2
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011
# Then the & operator compares the bits and returns 0010, which is 2 in decimal.

print(8 & 4) # 0
# 8 -> 00001000
# 4 -> 00000100
# ---------
# 0 -> 00000000


# The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:
print(6 | 3) # 7
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011
# Then the | operator compares the bits and returns 0111, which is 7 in decimal.


# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
print(6 ^ 3) # 5
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011
# Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.


# In Python, the bitwise NOT operator ~ flips all bits of a number
print(~6) # -7

"""
Using Bitwise NOT (~)

1. Convert 6 to binary (8-bit)
   6 = 00000110

2. Flip bits (~ operator)
   00000110 → 11111001 (1's Compliment)

3. Interpret as signed and convert to decimal (2’s Complement)
   11111001 → 00000110 (Reverse)
   00000110 + 1 = 00000111 = 7 (Add negative sign)
   So result = -7

Verify (Reverse Process)
    11111010 -> 00000101
    00000101 + 1 = 00000110 = +6

---------------------------------------
1. Write binary
2. Flip bits  (~ result)

3. Check MSB:
   If MSB = 1 → negative
       flip + add 1 → add minus sign

   If MSB = 0 → positive
       convert directly to decimal
---------------------------------------
MSB (Most Significant Bit)
0 → positive
1 → negative

Range (for n bits)
-128 to +127
---------------------------------------   
Shortcut Formula
    -n = 2’s complement of n
    ~n + 1 = -n  or  ~n = -(n + 1)

    For any number n:
    ~n = -(n + 1)

    n = 6
    ~6 = - (6 + 1) = -7

---------------------------------------
1’s Complement -> Flip all bits (0 → 1, 1 → 0)
    6 = 00000110
    1’s complement → 11111001
             Just invert bits

2’s Complement -> Flip bits + add 1
    6 = 00000110
    1’s complement → 11111001
    +1             → 11111010
                This gives -6

Super Shortcut (Very Important)
---------------------------------------
| Operation      | Shortcut           |
| -------------- | ------------------ |
| 1’s complement | `~n` (bitwise NOT) |
| 2’s complement | `~n + 1`           |
---------------------------------------

~6        # 1’s complement → -7
~6 + 1    # 2’s complement → -6

Key Difference (1 line)
    1’s complement → just flip bits
    2’s complement → flip bits + 1 (used for negatives)

Memory Trick
    1’s → Flip
    2’s → Flip + 1
"""

# ~6 = 11111001
# As unsigned → 249
print(0b11111001) # 249 |...11111001  (infinite bits)

# As signed (8-bit) → -7
# Convert to signed 8-bit manually
n = 0b11111001
if n >= 128:
    n -= 256
print(n) # -7

# ----------------------------------
# << (Left Shift)
"""
Shift bits left, add 0 on right
Equivalent to: multiply by 2ⁿ

x << 2   # x * 4
"""


# >> (Right Shift)
"""
Shift bits right, keep sign (copy MSB)
Equivalent to: divide by 2ⁿ (floor)

x >> 2   # x // 4
"""
# ----------------------------------
# Memory Trick
"""
    << → multiply
    >> → divide
"""

# Quick Rules
"""
<< → multiply (works same for negative)

>> → divide:
   positive → normal division
   negative → floor division (more negative)
"""
# ----------------------------------
print(5 << 1)   # 10 (5 * 2¹)
print(-5 << 1)  # -10 (-5 * 2¹)
print(5 >> 1)   # 2 (5 // 2¹)
print(-5 >> 1)  # -3 floor(-5 / 2¹) (sign preserved)
# 00000101(+5) -> 11111010 + 1(2's Compliment) -> 11111011(-5) -> ...11111011(Right Shift (>> 1)) -> ...11111101 -> ...00000010 + 1(2's Compliment) -> 00000011 -> 3 -> -3

"""
←—— -3 —— -2 —— -1 —— 0 —— 1 —— 2 ——→
floor(-2.1) = -3
floor(2.1)  = 2

Positive → remove decimal
Negative → go one more down

-5 >> 1 = floor(-5 / 2) = -3
"""
# ----------------------------------
print(3 << 5)
# 3 = 00000011
# 00000011 → 01100000
# 01100000 = 96

# Shortcut:
# 3 << 5 = 3 × 2⁵ = 3 × 32 = 96
# ----------------------------------
print(3 >> 5)
# 3 = 00000011
# 00000011 → 00000000
# 00000011 → 00000000

# Shortcut:
# 3 >> 5 = 3 // 2⁵ = 3 // 32 = 0
# ----------------------------------
import math
"""
math.floor(2.7)    # 2
math.floor(2.1)    # 2
math.floor(-2.1)   # -3
math.floor(-2.9)   # -3
"""
print(math.floor(-5 / 2*1))


# ===================| Python - Operators Precedence |===================
print('-------------------| Python - Operators Precedence |-------------------')

# Operator precedence describes the order in which operations are performed.

"""
Operator                                        Description
----------------------------------------------------------------------------------------------------
()	                                            Parentheses	
**	                                            Exponentiation
+x  -x  ~x	                                    Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                                    Multiplication, division, floor division, and modulus	
+  -	                                        Addition and subtraction	
<<  >>	                                        Bitwise left and right shifts	
&	                                            Bitwise AND	
^	                                            Bitwise XOR	
|	                                            Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	                                            Logical NOT	
and	                                            AND	
or	                                            OR
----------------------------------------------------------------------------------------------------
"""

# Example to Show Operator Precedence
print(
    (2 + 3) * 2 ** 2            # (), **
    + (-5)                      # unary -
    + (~3)                      # ~
    + (10 // 3) * (10 % 3)      # *, //, %
    + (1 << 2)                  # <<
    + (8 >> 2)                  # >>
    + (5 & 3)                   # &
    + (5 ^ 3)                   # ^
    + (5 | 3)                   # |
)

# Add Logical + Comparison
print(
    ((2 + 3) * 2 ** 2 > 10)     # comparison
    and not (5 == 3)            # not, and
    or (2 in [1, 2, 3])         # or, in
)

# Simple Combined Version (Readable)
print(
    2 + 3 * 2 ** 2 - ~3 << 1 & 7 ^ 2 | 1
)

'''
(((((2 + (3 * (2 ** 2)) - (~3)) << 1) & 7) ^ 2) | 1)

2 + 3 * 2 ** 2 - ~3 << 1 & 7 ^ 2 | 1
2 + 3 * 4 + 4 << 1 & 7 ^ 2 | 1
2 + 12 + 4 << 1 & 7 ^ 2 | 1
18 << 1 & 7 ^ 2 | 1
36 & 7 ^ 2 | 1

00100100 & 00000111 ^ 00000010 | 00000001
00000100 ^ 00000010 | 00000001
00000110 | 00000001
00000111 = 7
'''