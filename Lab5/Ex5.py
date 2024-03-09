import re
txt = input()
res = re.findall("^a.*b$",txt)
print(res)
