class Person:
    country = 'India'
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod # It is only a decorator 
    def gaming(cls):
        print('Mai India me rehta hu ! : ',cls.country)
        print("Bas Humko khelne me maja aata hai ")


Person.gaming()
per = Person('Awadh',99)
per.gaming()
print(Person.country)

'''
we can directly call it by class name only .
we can even class it with object.
it has the access to class property / state.

'''