'''
1. code reuse 
2. To denote relationship --- parent Child / Heirachical Relationship


isA for relationship checking    


'''

class Animal:
    def eat(self):
        print("Animal is eating")

class cat(Animal):
    pass

cat = cat()

cat.eat()