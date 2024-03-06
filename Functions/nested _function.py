def product(a,b):
    print(a*b)
    #sum(a,b)  --- It is incorrect because we need to define the function before its call
    def sum(a,b):
        print(a+b)
    sum(a,b)   


a , b = input().split()
a = int(a)
b = int (b)
product(a,b)


