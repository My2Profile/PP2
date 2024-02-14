#Python Format Strings

"""The format() method takes the passed arguments,
formats them, and places them in the string
where the placeholders {} are:"""

#1
age = 36
txt = "My name is John, I am " + age
print(txt)  #My name is John, and I am 36

#2

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  #My name is John, and I am 36

#3

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) #I want 3 pieces of item 567 for 49.95 dollars

#4

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#I want to pay 49.95 dollars for 3 pieces of item 567


#Python Escape Characters

#txt = "We are the so-called "Vikings" from the north."
#This will give syntax error as word Vikings is not covered by quotes
#To fix this we use \" char before the end of quote of the first sentence and end of our word
#\t -> tab 4 spaces; \b -> backspace remove previous one char
#form feed or \f used to indicate a start of new page for printer


#1

txt = "We are the so-called \"Vikings\" from the north."

#2

txt = "This will insert one \\ (backslash)."
print(txt) #This will insert one \ (backslash)

#3

txt = "This will insert one \\ (backslash)."
print(txt)

#4

txt = "Hello\nWorld!"
print(txt) """Hello
              World!"""

#5

txt = "Hello \bWorld!"
print(txt) #HelloWorld!

#6 Octal Value

txt = "\110\145\154\154\157"
print(txt) #Hello

#7 Hex value

txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #Hello
