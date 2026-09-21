# ===================| Python Sets |===================
print('-------------------| Python Sets |-------------------')

# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

# Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset) # {'cherry', 'apple', 'banana'} or {'apple', 'banana', 'cherry'} or {'cherry', 'banana', 'apple'},... can be any random order.

# ⦿ Note: Sets are unordered, so you cannot be sure in which order the items will appear.
# ⦿ Note: Set items are unchangeable, but you can remove items and add new items.

# Sets Items
#🔹Unordered
#🔹Unchangeable / Immutable
#🔹Unique Values
#🔹Unindexed

#🔹Duplicates Not Allowed
# Sets cannot have two items with the same value.
# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # 'apple', 'banana', 'cherry'} can be any random order

# ⦿ Note: The values True and 1 are considered the same value in sets, and are treated as duplicates.
# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0, 1, 2}
print(thisset) # {False, True, 2, 'apple', 'banana', 'cherry'} # 1 is not here

# ⦿ Note: The values False and 0 are considered the same value in sets, and are treated as duplicates.
# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0, 1, 2}
print(thisset) # {False, True, 2, 'apple', 'banana', 'cherry'} # 0 is not here


#🔹Set Length - len()
# To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) # 3

thisset = {"apple", "banana", "cherry", "apple", "banana"}
print(len(thisset)) # 3


#🔹Set Items - Data Types
# Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types like strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}


#🔹type()
# From Python's perspective, sets are defined as objects with the data type 'set':
# <class 'set'>

myset = {"apple", "banana", "cherry"}
print(type(myset)) # <class 'set'>


#🔹The set() Constructor
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # ⦿ Note the double round-brackets
print(thisset) # {"apple", "banana", "cherry"}


#🔹Python Collections (Arrays)
# There are four collection data types in the Python programming language:
"""
● List is a collection which is ordered and changeable. Allows duplicate members.
● Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
● Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
● Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# ===================| Python - Access Set Items |===================
print('-------------------| Python - Access Set Items |-------------------')

#🔹Access Sets Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


#🔹Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # True


#🔹Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset) # False


#🔹Change Items
# Once a set is created, you cannot change its items, but you can add new items.


# ===================| Python - Add Set Items |===================
print('-------------------| Python - Add Set Items |-------------------')

#🔹Add Items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.

# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) # {'cherry', 'banana', 'orange', 'apple'}


#🔹Add Sets
# To add items from another set into the current set, use the update() method.
# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) # {'papaya', 'cherry', 'banana', 'pineapple', 'apple', 'mango'}


#🔹Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# Add elements of a list to a set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) # {'apple', 'kiwi', 'orange', 'banana', 'cherry'}


# ===================| Python - Remove Set Items |===================
print('-------------------| Python - Remove Set Items |-------------------')

#🔹Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

#🔹Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # {'cherry', 'apple'}
# ⦿ Note: If the item to remove does not exist, remove() will raise an error.


#🔹Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) # {'apple', 'cherry'}
# ⦿ Note: If the item to remove does not exist, discard() will NOT raise an error.


# ou can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) # apple
print(thisset) # {'banana', 'cherry'}
# ⦿ Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.


#🔹The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # set()


#🔹The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # set()


# ===================| Python - Loop Sets |===================
print('-------------------| Python - Loop Sets |-------------------')

#🔹Loop Items
# You can loop through the set items by using a for loop.
# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


# ===================| Python - Join Sets |===================
print('-------------------| Python - Join Sets |-------------------')

#🔹Join Sets
"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

#🔹Union or |
# The union() method or | operator returns a new set with all items from both sets.
# ⦿ Note: The | operator only allows you to join sets with sets, and not with other data types like you can with the union() method.

# Use union() to join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) # {1, 'a', 2, 3, 'c', 'b'}

# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3) # # {1, 'a', 2, 3, 'c', 'b'}


# Join Multiple Sets
# All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, separated by commas.

# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset) # {'c', 1, 2, 3, 'John', 'Elena', 'b', 'apple', 'bananas', 'cherry', 'a'}

# When using the | operator, separate the sets with more | operators:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset) # {'c', 1, 2, 3, 'John', 'Elena', 'b', 'apple', 'bananas', 'cherry', 'a'}


#🔹Join a Set and a Tuple using union() method:
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z) # {1, 2, 3, 'a', 'c', 'b'}
# ⦿ Note: The | operator only allows you to join sets with sets, and not with other data types.


#🔹Update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) # {'b', 'c', 1, 2, 3, 'a'}
# ⦿ Note: Both union() and update() will exclude any duplicate items.


#🔹Intersection or &
# Keep ONLY the duplicates
# The intersection() method or & operators will return a new set, that only contains the items that are present in both sets.
# ⦿ Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# Use intersection() to join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3) # {'apple'}

# Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3) # {'apple'}


# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1) # {'apple'}


# The values True and 1 are considered the same value. The same goes for False and 0.
# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {0, 1, "apple", "banana", "cherry"}

set2 = {False, 0, 1, True, "google", 1, "apple", 2}
setOutput = set1.intersection(set2)
print(setOutput) # {False, 1, 'apple'} 

set2 = {False, True, "google", "apple", 2, 0, 1}
setOutput = set1.intersection(set2)
print(setOutput) # {False, True, 'apple'}

set3 = {0, 1, 2, "google", "apple", False, True}
setOutput = set1.intersection(set2, set3)
print(setOutput) # {False, True, 'apple'}

# ⦿ Note:
# In Python, True == 1 and False == 0, so they are treated as duplicate values in a set.
# A set keeps only the first occurrence and ignores the rest.
# During intersection, if both equivalent values exist (True & 1 or False & 0), the result will include the one that appears first in set2, If multiple then second Set.


#🔹Difference
