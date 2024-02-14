def result(list_numbers,size):
    for i in range(size):
     if i==size-1:
       return "False"
     if list_numbers[i]=="3" and list_numbers[i+1]=="3":
       return "True"
    

list_numbers=[]
size=int(input())
for i in range(size):
    num=input()
    list_numbers.append(num)

print(result(list_numbers,size))
