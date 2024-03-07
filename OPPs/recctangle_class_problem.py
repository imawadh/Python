class Rectangle :
    def __init__(self,length, breadth):
        self.__lenght = length
        self.__breath = breadth 

    

    def getarea(self):
        return self.__breath* self.__lenght
    
    def getperimeter(self):
        return 2*(self.__breath + self.__lenght)
    
    def setlenght(self,length):
        self.__lenght = length
        

    def setbreadth(self, breadth):
        self.__breath = breadth 




