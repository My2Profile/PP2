#Loop Dictionaries

#1

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
#brand  model   year

#2

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
#Ford   Mustang     1964

#3

for x in thisdict.values():
  print(x)
#Ford   Mustang     1964

#4

for x in thisdict.keys():
  print(x)
#brand  model   year

#5

for x, y in thisdict.items():
  print(x, y)
"""
brand Ford
model Mustang
year 1964
"""


                                    #Copy Dictionaries
#1

mydict = thisdict.copy()
print(mydict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#2

mydict = dict(thisdict)
print(mydict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


                                    #Nested Dictionaries
#1

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
"""
{'child1': {'name': 'Emil', 'year': 2004},
'child2': {'name': 'Tobias', 'year': 2007},
'child3': {'name': 'Linus', 'year': 2011}}
"""

#2

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
"""{'child1': {'name': 'Emil', 'year': 2004},
'child2': {'name': 'Tobias', 'year': 2007},
'child3': {'name': 'Linus', 'year': 2011}}"""

#3

print(myfamily["child2"]["name"])
#Tobias


                                    #Dictionary Exercise
#1

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#2

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#3

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#4

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#5

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
