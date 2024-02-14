def histogram(x,y):
    r=""
    for i in range(size):
        a=int(list_numbers[i])
        while a!=0:
            r+="*"
            if a==1:
                print(r)
                r=""

            a-=1
            


list_numbers=[]
size=int(input())
for i in range(size):
    n=input()
    list_numbers.append(n)

histogram(list_numbers,size)