def spy_game(x,y):
    cnt=0
    for i in range(size):
        if list_numbers[i]=="0":
            cnt+=1
        if cnt==2 and list_numbers[i]=="7":
            return "True"
        if i==size-1:
            return "False"


list_numbers=[]
size=int(input())
for i in range(size):
    num=input()
    list_numbers.append(num)

print( spy_game(list_numbers,size))  