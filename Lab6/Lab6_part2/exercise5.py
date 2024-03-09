tuple_=(1,1,1,True,"nnjnn")
cnt=0
for i in tuple_:
    if i==True:
       cnt+=1

if cnt==len(tuple_):
    print("True")
else:
    print("False")
       