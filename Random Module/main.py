print("Hello World")
import random # importing random module 
'''
We use random module  to generate random number or captcha code and ludo game.
 we can even import it as from random import random
'''

# random() -- generate random real number from [0,1). we do not need to pass any argument.

print(random.random()) # we can give any range 

'''
randrange(lower limit ,upper limit )
it generates number from[lower limit, upper limit)
'''
print(random.randrange(1000,10000))

import random as awadh
print(awadh.randrange(122,345))