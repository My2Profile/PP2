import re
text=input()
result=""
cnt=0
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in text:
    for j in alphabet:
        if i==j:
            result+=" "
            cnt+=1
    
    if cnt==0:
        result+=i
    else:
        cnt=0


print(result)
