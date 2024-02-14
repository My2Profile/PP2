                                #Python Operators 
                                #Exercise

#1

print(10+5)     #15


#2

x = 5
y = 3

print(x + y)    #8

#3

x = 5
y = 3

print(x - y)    #2

#4

x = 5
y = 3

print(x * y)    #15

#5

x = 12
y = 3

print(x / y)    #4

#6

x = 5
y = 2

print(x % y)    #1

#7

x = 2
y = 5

print(x ** y) #32

#8

x = 15
y = 2

print(x // y)   #7

#the floor division // rounds the result down to the nearest whole number

#9

x = 5

x &= 3

print(x)    #1

#10

x = 5

x |= 3

print(x)    #7

#11

x = 5

x ^= 3

print(x)    #6  Bitwise XOR operator

#12

x = 5

x >>= 3

print(x)    #0  Same as 5/2^3

#13

x = 5

x <<= 3

print(x)    #40 #Same as 5*2*2*2=40

#14

x = 5
y = 3

print(x == y)   # returns False because 5 is not equal to 3

#15

x = 5
y = 3

print(x != y)   # returns True because 5 is not equal to 3

#16

x = 5
y = 3

print(x > y)    # returns True because 5 is greater than 3

#17

x = 5
y = 3

print(x < y)    # returns False because 5 is not less than 3

#18

x = 5
y = 3

print(x >= y)   # returns True because five is greater, or equal, to 3

#19

x = 5
y = 3

print(x <= y)
# returns False because 5 is neither less than or equal to 3

                                        #lOGICAL oPERANDS

#20

x = 5

print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

#21

x = 5

print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)


#22

x = 5

print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

                                        #Python Identity Operators
                                        #Same if have same mem location
#1

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#2

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

                                        #Python Memebership Operators

#1

x = ["apple", "banana"]

print("banana" in x)    #True


#2

x = ["apple", "banana"]

print("pineapple" not in x)     #True

#4

print(100 + ~3)     #96 (100-4)
#

                                        #Exercises
#1

print(10*5)     #50

#2

print(10/2)     #5

#3

fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")
""""""

#4

if 5!=10:
    print("5 does not equal 10")
""""""

#5

if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")
""""""
