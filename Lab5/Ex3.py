import re
text = input()
result = re.findall("[a-z]_[a-z]", text)
print(result)
