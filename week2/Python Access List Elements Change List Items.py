#Python Access List Elements 

#1

thislist = ["apple", "banana", "cherry"]
print(thislist[1])  #banana

#2

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])     #cherry

#3

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])    #['cherry', 'orange', 'kiwi']

#4

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])     #['apple', 'banana', 'cherry', 'orange']

#5

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])     #['cherry', 'orange', 'kiwi', 'melon', 'mango']

#6

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  #['orange', 'kiwi', 'melon']

#7

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")   #Yes, 'apple' is in the fruits list


                                      #Python - Change List Items

#1

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)           #['apple', 'blackcurrant', 'cherry']

#2

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)           #['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

#3

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)           #['apple', 'blackcurrant', 'watermelon', 'cherry']

#4

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)           #['apple', 'blackcurrant', 'watermelon', 'cherry']

#6

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)           #['apple', 'watermelon']

#5

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)             #['apple', 'banana', 'watermelon', 'cherry']
