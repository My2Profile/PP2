#Python Join Sets

#1

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#

#2

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)#inserts items into set 1
#

#3

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y) #Items that exist in both sets

print(x)
#

#4

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) #Items that exist in both sets

print(z)


#5

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y) #Items that are not present in both

print(x)


#6

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)   #XOR dont contain intersection

print(z)


#7

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)
#


                                        #Set Exercises
#1

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#2

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#3

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#4

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#5

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
