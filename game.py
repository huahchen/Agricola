class Game:
    def __init__(self, numPlayers, deck):
        self.numPlayers = numPlayers # May change to more later
        self.deck = deck
        self.playerAbilities = {}
        self.loadMajors()

    def loadOccs(self):
        f = open('occ.txt', 'r')
        line = f.readline()
        while (line != ""):
            print line
            line = f.readline()

    def loadMajors(self):
        f = open('major.txt', 'r')
        

#def genMinors(self):

a = Game()
a.genOccs()

