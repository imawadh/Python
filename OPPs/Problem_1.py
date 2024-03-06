class Point:
    def __init__ (self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def square_sum(self):
        print(self.x**2 + self.y**2 + self.z**2)


value = Point(2,3,5)
value.square_sum()