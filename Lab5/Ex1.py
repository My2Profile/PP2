import re
text = input()
result = re.findall("ab*", text)
print(result)
