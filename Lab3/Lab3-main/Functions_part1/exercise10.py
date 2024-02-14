def unique(x,y,):
    unique_numbers={}
    for i in range(size):
        unique_numbers[list_numbers[i]]=1
        if i==size-1:
            x=list(unique_numbers.keys())
            return str(x).replace("[","").replace("]","").replace(",","").replace("'","")

list_numbers=[]
size=int(input())
for i in range(size):
    num=input()
    list_numbers.append(num)

print(unique(list_numbers,size)) 