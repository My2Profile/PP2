#Python Strings 
print("Hello", 'Hello', sep='\n') #"Hello" == 'Hello'

#1

a= "Hello"
print(a) #Hello

#2

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) #Lorem ipsum dolor sit amet,consectetur adipiscing elit,sed do eiusmod tempor incididuntut labore et dolore magna aliqua.

""" used """""" to enter multiline comment or long commments no difference in
"""""" and '''''' as both have same func in python """ 

#3

a = "Hello, World!"
print(a[1])     #string is array of chars and output will be e as index starts from 0


#4


for x in "abc":
  print(x)
""" a
    b
    c"""

#5
a = "Hello, World!"
print(len(a)) #13 space bar is also counted

#6

txt = "The best things in life are free!"
print("free" in txt)    #boolean as it returns true in our case as string contains the word

#7

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")      #condition if true code will be executed code is print


#8

txt = "The best things in life are free!"
print("expensive" not in txt)   #if expensive not in text returns True

