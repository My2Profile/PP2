#Python Lists 

#1

mylist = ["apple", "banana", "cherry"]

#2

thislist = ["apple", "banana", "cherry"]    #['apple', 'banana', 'cherry']
print(thislist)

#3

thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)     #['apple', 'banana', 'cherry', 'apple', 'cherry']

#4

thislist = ["apple", "banana", "cherry"]
print(len(thislist))    #3

#5

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)    #['apple', 'banana', 'cherry']
print(list2)    #[1, 5, 7, 9, 3]
print(list3)    #[True, False, False]

#6

list1 = ["abc", 34, True, 40, "male"]

print(list1)    #['abc', 34, True, 40, 'male']

#7

mylist = ["apple", "banana", "cherry"]
print(type(mylist))     #class list

#8

thislist = list(("apple", "banana", "cherry"))
print(thislist)     #thislist = ["apple", "banana", "cherry"]


