'''
for the exquation 2x - 5y = 0

find the  pair of value possible :
at y =  1,2,3,4,6,7,9,90

solving the equation we get x = 5y/2

'''
def f(y):
    return 5*y/2

y =  [1,2,3,4,6,7,9,90]

for i in y:
    a = f(i)
    print(i,a)

