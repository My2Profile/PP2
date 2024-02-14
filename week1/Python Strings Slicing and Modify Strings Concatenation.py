#Python Strings Slicing
#Accessing different chars
a = "Hello, World!"
print(a[2:5])   #ll0 works like [2:5)
print(a[:5])    #Hello
print(a[2:])    #llo, World!
print(a[-5:-2])     #-1 starts from end ->! thus [-5:-2] ->orl works like [-5:-2)


#Python Modify Strings

#1)

a = "Hello, World!"
print(a.upper())     # HELLO, WORLD!

#2)

a = "Hello, World!"
print(a.lower())    # hello, world!

#3)

a = "   Hello, World!   "
print(a.strip())    # Hello, World!

#4)

a = "Hello, World!"
print(a.replace("H", "J"))  #Jello, World!
#sensitive case: a = "Hello, Horld!" replace will return "Jello, Jorld!"

#5)

a = "Hello, World!"
b = a.split(",")
print(b) #returns list of seperated words -> ['Hello', 'World!']
#sensitive case: will work for strings like ip
#EX: 192.168.0.0.0 print(split(".")) returns ['192','168','0','0','0']

#Python String Concatenation
a,b = "Hello", "World"
c = a + b
print(c)     #HelloWorld
c= a + " " + b
print(c)     #Hello World
