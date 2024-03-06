# class is the keyword and Person is the name of class 
'''

class name consideration is same as variable name decleartion
class name should start with capital letter it is convention only not rule 


'''
class Person : 
    pass

per_object = Person()
print(per_object)


class Man:
    # logic to create object with attribute 
    # Initializer
    def __init__(self, name , age): # only init can be there in a class if we declear many init function function we will not get any error but will only consider last init method 
        # self is only convention 
        self.name = name
        self.age = age

per = Man("Awadh Kishor Singh",90)
print(per.name)
print(per.age)