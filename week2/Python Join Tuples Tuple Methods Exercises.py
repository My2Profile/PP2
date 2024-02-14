#Python Join Tuples
#Examples

#1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#('a', 'b', 'c', 1, 2, 3)

#2

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
#('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


                                    #Tuple Methods
#1
"""
count() --> Returns the number of times a specified value occurs in a tuple

index() --> 	Searches the tuple for a specified value
and returns the position of where it was found
"""

                                    #Tuple Exercises

#1

fruits = ("apple", "banana", "cherry")
print(fruits[0])

#2

fruits = ("apple", "banana", "cherry")
print(len(fruits))

#3

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#4

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:6])
