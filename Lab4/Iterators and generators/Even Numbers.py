def gen2(n):
    for i in range(n+1):
        if i%2==0:
            yield i

a=int(input())
b=gen2(a)
for i in gen2(a):
    print(i,end=", ")
