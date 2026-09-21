# ===================| Python - Collection Data Types |===================
print('-------------------| Python - Collection Data Types |-------------------')

"""
In Python, the 4 main built-in collection data types are:
🔹List
🔹Tuple
🔹Set
🔹Dictionary

Here’s a clear comparison table 👇

Feature	                List	               Tuple	             Set	                Dictionary
----------------------------------------------------------------------------------------------------------------------
Syntax	                [ ]                    ( )	                 { }	                {key: value}
Example	                [1, 2, 3]              (1, 2, 3)	         {1, 2, 3}	            {"a": 1, "b": 2}
Ordered	                ✅ Yes                 ✅ Yes	              ❌ No	                ✅ Yes (Python 3.7+)
Mutable	                ✅ Yes                 ❌ No	              ✅ Yes	                ✅ Yes
Allows Duplicates	    ✅ Yes                 ✅ Yes	              ❌ No	                ❌ Keys: No (Values: Yes)
Indexing	            ✅ Yes                 ✅ Yes	              ❌ No	                ❌ (use keys)
Key-Value Pair	        ❌ No                  ❌ No                ❌ No	                ✅ Yes
Heterogeneous Data	    ✅ Yes                 ✅ Yes               ✅ Yes	                ✅ Yes
Performance	            Slower than tuple	   Faster than list      Fast for membership	Fast key lookup
Use Case	            Dynamic collection	   Fixed data	         Unique items	        Mapping data
----------------------------------------------------------------------------------------------------------------------

Quick Understanding
🔹List → Use when you need changeable (mutable) ordered data
🔹Tuple → Use when data should be fixed (immutable)
🔹Set → Use when you need unique elements only
🔹Dictionary → Use when working with key-value pairs

"""

# Example Code

# List
l = [1, 2, 2, 3]
print(l)
print(l[0])
# ------------------------------------

# Tuple
t = (1, 2, 2, 3)
print(t)
print(t[0])
# ------------------------------------

# Set
s = {1, 2, 2, 3}   # duplicates removed
print(s)

# set is unordered → no indexing
for item in s:
    print(item)

print(list(s)[0])   # not reliable order
print(2 in s)   # True
# ------------------------------------

# Dictionary
d = {"a": 1, "b": 2}

# Using []
print(d["a"])      # 1 | d[key]
# print(d["c"])    # ❌ KeyError

# Using get() - Safe to use
print(d.get("a"))       # 1    | d.get(key)
print(d.get("c"))       # None | (no error)
print(d.get("c", 3))    # 3    | d.get(key, default)
print(d) # {"a": 1, "b": 2}

# setdefault()
print(d.setdefault("c", 3))
print(d) # {"a": 1, "b": 2, "c": 2}


# 📊 Difference Table
"""
Feature            d[key]                    d.get(key)                 d.setdefault(key, default)
-------------------------------------------------------------------------------------------------------
Purpose            Direct access             Read value safely            Read + insert if missing
Access style       Direct indexing           Method call                  Method call
Key exists         ✅ Returns value          ✅ Returns value            ✅ Returns value
Key missing        ❌ KeyError               ✅ Returns None             ✅ Adds key + returns default
Default value      ❌ Not supported          ✅ Supported                ✅ Supported
Modifies dict      ❌ No                     ❌ No                       ✅ Yes
Safety             ❌ Unsafe                 ✅ Safe                     ✅ Safe (but modifies)
Use case           When key is guaranteed    When key may/may not exist   Initialize missing keys
-------------------------------------------------------------------------------------------------------

🧠 Final Interview Line (Best Answer)
🔹 d[key] → Direct but unsafe
🔹 d.get() → Safe read
🔹 d.setdefault() → Safe + inserts missing key
"""