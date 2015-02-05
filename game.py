from random import shuffle
class Game:
    def __init__(self, numPlayers, deck):
        self.numPlayers = numPlayers # May change to more later
        self.deck = deck
        self.playerAbilities = {}
        self.loadMajors()
        self.roundCards = [["1Sow/Bake", "1Sheep", "1Major", "1Fence"], ["2Reno", "2Growth", "2Stone"], ["3Boar", "3Vegetable"], ["4Cattle", "4Stone"], ["5Plow/Sow", "5Growth"], ["6Reno"]]
        self.shuffle(self.roundCards)

    def shuffle(self, roundCards):
        for x in roundCards:
            shuffle(x)
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

