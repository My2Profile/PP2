#Python Variable Exercises 
carname = "Volvo"
x = 50

x = 5
y = 10
print(x+y) #15

x = 5
y = 10
z=x+y
print(z) #15

x,y,z = "Orange", "Banana", "Cherry" #x=Orange y=Banana z=Cherry


x = y = z = "Orange"

def myfunc():
    global x
    x = "fantastic"

