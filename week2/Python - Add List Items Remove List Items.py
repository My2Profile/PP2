                                #Python - Add List Items 

#1

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#['apple', 'banana', 'cherry', 'orange']

#2

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#['apple', 'orange', 'banana', 'cherry']

#3

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


#4

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#['apple', 'banana', 'cherry', 'kiwi', 'orange']


                                #Python Remove List Items

#1

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry']

#2

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry', 'banana', 'kiwi']

#3

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#['apple', 'cherry']

#4

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#['apple', 'banana']

#5

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#['banana', 'cherry']

#6

thislist = ["apple", "banana", "cherry"]
del thislist        #Deletes Entire list

#7

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)     #thislist=[]
