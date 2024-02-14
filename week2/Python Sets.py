#Python Sets

#1

thisset = {"apple", "banana", "cherry"}
print(thisset)
#{'banana', 'apple', 'cherry'}

#2

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#{'banana', 'cherry', 'apple'}

#3

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#{True, 2, 'banana', 'cherry', 'apple'}

#4

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#{False, True, 'cherry', 'apple', 'banana'}

#5

thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#3

#6
set1 = {"apple", "banana", "cherry"}    #{'cherry', 'apple', 'banana'}
set2 = {1, 5, 7, 9, 3}  #{1, 3, 5, 7, 9}
set3 = {True, False, False}     #{False, True}

#7

set1 = {"abc", 34, True, 40, "male"}
#{True, 34, 40, 'male', 'abc'}

#8

myset = {"apple", "banana", "cherry"}
print(type(myset))
#class set

#9

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#Unordered set
#{'cherry', 'banana', 'apple'}
