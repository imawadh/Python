class Car:
    country = "Made in India"
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def brand_name(self):
        print(self.brand+" is " + self.color + " is accelarating")

car_obj = Car("BMW",'red')
car_obj.brand_name()