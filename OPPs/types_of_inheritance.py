'''
1. Simple Inhetitance --- A single child parent relationship
2. Method overwriting ---- 2 same method present in  parent child as well
   super keyword is used to call the same method present in the parent class
   
    

'''

class Parent :
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("All of us eat food .")


class Child(Parent):
    def __init__(self,name,breed):
        Parent.__init__(self,name) # Created parent first
        self.breed = breed

dog = Child('Tommy','Vodafone')


dog.eat()
