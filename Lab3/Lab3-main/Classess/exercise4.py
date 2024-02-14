class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def show(self):
         print(self.x,self.y)

    def move(self):
        self.x=self.x-5
        self.y=self.y-5
        print(self.x,self.y)

    def dist(self):
        self.point2x=3
        self.point2y=7
        self.distance_x=self.point2x-self.x
        self.distance_y=self.point2y-self.y
        if self.distance_x>0 and self.distance_y>0:
            print(self.distance_x,self.distance_y)
        else:
            if self.distnace_x>0:
                print(self.distnace_y*-1)
            elif self.distance_x<0 and self.distance_y<0:
                print(self.distance_x*-1,self.distance_y*-1)

            else:
                print(self.distnace_y*-1)
           

x=int(input())
y=int(input())
points=Point(x,y)
points.show()
points.move()
points.dist()