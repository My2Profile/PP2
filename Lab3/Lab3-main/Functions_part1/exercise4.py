def filter_primes(numbers):
    for i in numbers:
        if int(i)%2!=0:
            print(i)


size=int(input())
numbers=[]
for i in range(size):
    num=input()
    numbers.append(num)

filter_primes(numbers)
