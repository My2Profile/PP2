def down(n):
    while n>=0:
        yield n
        n-=1

a=int(input())
for x in down(a):
    print(x, end=", ")
