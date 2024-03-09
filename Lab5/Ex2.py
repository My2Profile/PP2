import re
text = input()
result = re.findall("abb|abbb", text)
print(result)
