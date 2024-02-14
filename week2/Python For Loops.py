#Python For Loops
#Examples

#1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#apple banana cherry sep='\n'

#2

for x in "banana":
    print(x)
#b a n a n a; sep='\n'

#3

for x in fruits:
  print(x)
  if x == "banana":
    break
#apple banana; sep='\n'

#4

for x in fruits:
  if x == "banana":
    break
  print(x)
#apple

#5

for x in fruits:
    if x == "banana":
        continue
    print(x)
#apple cherry; sep='\n'

#6

for x in range(6):
  print(x)
#0 1 2 3 4 5; sep='\n'

#7

for x in range(2,6):
    print(x)
#2 3 4 5; sep='\n'

#8

for x in range(2, 30, 3):
  print(x)
#2 5 8 11 14 17 20 23 26 29; increment = 3;

#9

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#10

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#0 1 2
  #loop stopped by break; No execution of else

#11

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#red apple; red banana; red cherry; sep = '\n'
#big apple; big banana; big cherry; sep = '\n'
#tasty apple; tasty banana; tasty cherry; sep = '\n'

#12

for x in [0, 1, 2]:
  pass
#Nothing happens



                                        #Python Exercises

#1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2

for x in fruits:
    if x == "banana":
        continue
    print(x)

#3

for x in range(6):
    print(x)

#4

for x in fruits:
    if x == "banana":
        break
    print(x)
    
