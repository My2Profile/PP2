#Python Add Set Items

#1

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#{'orange', 'banana', 'apple', 'cherry'}

#2

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#3

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#{'banana', 'cherry', 'apple', 'orange', 'kiwi'}


                                #Remove Set Items

#1

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#{'cherry', 'apple'}

#2

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#{'apple', 'cherry'}

#3

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#apple
#{'cherry', 'banana'}

#4

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#set()

#5

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
#Complete Delete the Set --> NameError: name 'thisset' is not defined


                                    #Loop Sets

#1

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#cherry  banana  apple
