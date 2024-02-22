class parallelogram():
    def __init__(self,length,height):
        self.length=length
        self.height=height
        self.area=self.length*self.height




a=int(input("Length of base: "))
b=int(input("Height of parallelogram: "))

p=parallelogram(a,b)
print("Expected Output: ",p.area)
