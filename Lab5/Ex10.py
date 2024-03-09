import re
text = input()
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ""
for i in text:
    for j in alph:
        if i==j:
            res = res+"_"+i.lower()
            cnt+=1
    if cnt == 0:
        res=res+i
    else:
        cnt=0
print(res)
