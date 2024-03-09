import re
txt = input()
result = txt.replace(" ",";").replace(",",";").replace(".",";")
print(result)
