class Person:
    country = 'India'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def mass_bunking():
        print('Mass Bunking me kya hi maja hai')



Person.mass_bunking()
per = Person('Awadh',79)
per.mass_bunking()

'''
No need of any argument 
if required we provide it

It doesnot have access to class or state 

'''