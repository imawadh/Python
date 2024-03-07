'''
Acess Modifiers
1. Public --- Acess to everyone
2. Private --- Internally


'''

class Cricket:
    def __init__(self,player1,player2,fight):
        self.player1=player1
        self.player2=player2
        self.__fight = fight # it is private 


    def play(self):
        print(self.player1,'is copy cricket player')

object1 = Cricket('Virat','Gambhir','IPL was one of such instances ... ')
print(object1.player1)
