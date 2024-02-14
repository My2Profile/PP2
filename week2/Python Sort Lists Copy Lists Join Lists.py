#Python Sort Lists 

#1

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#'banana', 'kiwi', 'mango', 'orange', 'pineapple'

#2

thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)
#23, 50, 65, 82, 100

#3

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist)
#'pineapple', 'orange', 'mango', 'kiwi', 'banana'

#4

thislist = [100, 50, 65, 82, 23]

thislist.sort(reverse = True)

print(thislist)
#100, 82, 65, 50, 23

#5

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)
#50, 65, 23, 82, 100 -> Depending on how close number is to 50

#6

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist)
#'Kiwi', 'Orange', 'banana', 'cherry'
#Case sensitive sorting

#7

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#'banana', 'cherry', 'Kiwi', 'Orange'
#Case insensitive sorting

#8

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist)
#'cherry', 'Kiwi', 'Orange', 'banana'
#reverses the current sorting in this case "banana", "Orange", "Kiwi", "cherry"


                                    #Python Copy Lists


#1

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#'apple', 'banana', 'cherry'

#2

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#'apple', 'banana', 'cherry'


                                    #Python Join Lists

#1

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#'a', 'b', 'c', 1, 2, 3

#2

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#'a', 'b', 'c', 1, 2, 3

#3

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#'a', 'b', 'c', 1, 2, 3
