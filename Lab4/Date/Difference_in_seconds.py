import datetime
x=datetime.datetime.now()
x=x.strftime("%S")
e=int(x)
print("Input a time as DD:MM:SS")
s = input()
s=s.split(":")
d=s[2]
print("Difference in seconds is ",e-int(d))
