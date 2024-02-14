#Python Update Tuples 
#Examples

#1

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#("apple", "kiwi", "cherry")

#2

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#('apple', 'banana', 'cherry', 'orange')

#3

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#('apple', 'banana', 'cherry', 'orange')

#4

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#('banana', 'cherry')

#5

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
#name 'thistuple' is not defined


                                        #Unpack Tuples
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

#1

fruits = ("apple", "banana", "cherry")
#'apple', 'banana', 'cherry'

#2

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green,yellow,red,sep='\n',end='\n')
#apple banana cherry

#3
#If the number of variables is less than the number of values, you can add an * to the
#variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green,yellow,red,sep='\n',end='\n')
#apple      banana      ['cherry', 'strawberry', 'raspberry']

#4

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green,*tropic,red,sep='\n',end='\n')
#apple      ['mango', 'papaya', 'pineapple']        cherry


                                        #Loop Tuples
#Examples

#1

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#apple   banana     cherry

#2

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#apple   banana    cherry

#3

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#apple   banana     cherry
