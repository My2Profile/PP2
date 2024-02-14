#Python Dictionaries

#1

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#2

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#Ford

#3

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#No items with same key last will be applied
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#4

print(len(thisdict))    #3

#5

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
#{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

#6

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#class dict

#7

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
#{'name': 'John', 'age': 36, 'country': 'Norway'}


                                        #Accessing Items

#1

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#Mustang

#2

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
#Mustang

#3

x = thisdict.keys()
#dict_keys(['brand', 'model', 'year'])

#4

x = car.keys()

print(x) #before the change
#dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change
#dict_keys(['brand', 'model', 'year', 'color'])

#5

x = thisdict.values()
#dict_values(['Ford', 'Mustang', 1964])

#6

x = car.values()

print(x) #before the change
#dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x) #after the change
#dict_values(['Ford', 'Mustang', 2020])

#7

x = car.values()

print(x) #before the change
#dict_values(['Ford', 'Mustang', 1964])

car["color"] = "red"

print(x) #after the change
#dict_values(['Ford', 'Mustang', 1964, 'red'])

#8


x = thisdict.items()

print(x)
#dict_items([('brand', 'Ford'),('model', 'Mustang'),('year', 1964), ('color', 'red')])

#8
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  #True



                                    #Add Items

#1

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

                                    #Remove Dictionary Items

#1

thisdict.pop("model")
print(thisdict)
#{'brand': 'Ford', 'year': 1964}

#2
thisdict.popitem()
print(thisdict)
#Deletes Random Item before 3.7 after removes last item

#3

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#{'brand': 'Ford', 'year': 1964}

#4

"""del thisdict
print(thisdict)
Completely delets the dictionary"""

#5

"""thisdict.clear()
print(thisdict)
Empties The Dictionary"""
