#Python Update Tuples 
#Examples

#1

thistuple = ("apple", "banana", "cherry")
print(thistuple)
#"apple", "banana", "cherry"

#2

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#"apple", "banana", "cherry", "apple", "cherry"

#3

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#3

#4

thistuple = ("apple",)
print(type(thistuple))
#class tuple

"""#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) --> class str"""

#5

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
"""('apple', 'banana', 'cherry')
(1, 5, 7, 9, 3)
(True, False, False)"""

#6

tuple1 = ("abc", 34, True, 40, "male")
#('abc', 34, True, 40, 'male')

#7

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#<class 'tuple'>

#8

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#('apple', 'banana', 'cherry')



                                #Access Tuples
#Examples

#1

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#banana

#2

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#cherry

#3

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#('cherry', 'orange', 'kiwi')

#4

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#('apple', 'banana', 'cherry', 'orange')

#5

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#('cherry', 'orange', 'kiwi', 'melon', 'mango')

#6

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#('orange', 'kiwi', 'melon')

#7

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#Yes, 'apple' is in the fruits tuple



