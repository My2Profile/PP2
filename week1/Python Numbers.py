#Python Numbers 
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#2
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#3
x = 1.10
y = 1.0
z = -35.59

print(type(x))  #class float
print(type(y))
print(type(z))

#4
x = 35e3
y = 12e4
z = -87.7e100

print(type(x)) #class float
print(type(y))
print(type(z))

#5
x = 3+5j
y = 5j
z = -5j

print(type(x))  #class complex
print(type(y))
print(type(z))

#6
x = float(1)
y = int(2.8)
z = complex(1)

print(x)    #1.0
print(y)    #2
print(z)    #1+0j imaginary part -> 0j "0" as it was not entered

print(type(x))  #class float
print(type(y))  #class int
print(type(z))  #class complex

import random
print(random.randrange(1,10)) #random number from interval [1,10]


#Exercises

x = 5
x = float(x)    #5 -> 5.0

x = 5.5
x = int(x)  # 5.5 -> 5
