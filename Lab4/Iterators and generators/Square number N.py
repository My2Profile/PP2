def gen(number):
    for i in range(number):
        yield i**2

a=int(input())
b=gen(a)
for i in range(a):
    print(next(b))
