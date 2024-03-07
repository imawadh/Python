class Car:
    city = 'Banglore'
    def __init__ (self, a , b):
        self.a = a
        self.b = a
        """
        Here, a, b are object/instance variable 
        City is the object variable
        print(car1_object) gives the address of (car1_object) object in the memmory
        
        """

car1_object = Car(1,2)
print(car1_object)