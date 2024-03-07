'''
Encapsulation is the binding together of data and the method


1. state and field of must be made private.
2. methods must be public


'''

class Person:
    def __init__(self,name,car):
        self.__name = name
        self.__car = car

    def getName(self):
        return self.name
        
    def setName(self,name):
        self.__name = name

    def getCar(self):
        return self.__car
    
    def setCar(self,car):
        self.__car = car