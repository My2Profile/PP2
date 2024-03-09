word=input()
big_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_letters="abcdefghijklmnopqrstuvwxyz"
cnt1_big=0
cnt2_small=0
cnt0=0
for i in word:
    for j in big_letters:
        if i==j and cnt0==0:
            cnt1_big+=1
    for k in small_letters:
        if i==k and cnt0==0:
            cnt2_small+=1
    cnt0=0
print(cnt1_big,cnt2_small)

