class Shape:
    def area(self):
        print(0)


class Square(Shape):
    def __init__(self,length):
        self.length=length
        



p=Shape()
p.area()
p=Square(5)
p.area()