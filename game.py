from random import shuffle
from board import *
from player import Player

class Game:
    def __init__(self, numPlayers, deck):
        #players
        self.numPlayers = numPlayers # May change to more later
        self.players = []
        for x in range(numPlayers):
            self.players.append(Player())

        #occs and improvements
        self.deck = deck
        self.loadMajors()

        #round cards
        self.roundCards = [["1Sow/Bake", "1Sheep", "1Major", "1Fence"], ["2Reno", "2Growth", "2Stone"], ["3Boar", "3Vegetable"], ["4Cattle", "4Stone"], ["5Plow/Sow", "5Growth"], ["6Reno"]]
        self.shuffle(self.roundCards)

        #accumulating spaces
        self.3wood = []
        self.clay = []
        self.reed = []
        self.fishing = []
        self.sheep = []
        self.boar = []
        self.cattle = []
        self.stoneR2 = []
        self.stoneR6 = []

    def shuffle(self, roundCards):
        for x in roundCards:
            shuffle(x)

    def loadOccs(self): #TODO
    def loadMajors(self): #TODO

    def checkSubtract(self, *args):
        #check
        for x in args:
            if x[0] < x[1]:
                return 1
        #subtract
        for x in args:
            x[0] -= x[1]
    
    #action spaces
    def build(self, player, numRooms, numStables):
        wood = 0
        #check material of player's home
        roomType = player.board[0][2].type 
        if roomType == SquareType.woodenRoom:
            wood += 5 * numRooms
        elif roomType == SquareType.clayRoom:
            clay = 5 * numRooms
        else:
            stone = 5 * numRooms
        #reed cost
        reed = 2 * numRooms
        #stable cost
        wood += 2 * numStables

        #apply effects
        
        #create tuplist

        #check & subtract
        #if checkSubtract(tupList) != 1:
    def startingPlayer(self, player):

test = Game(1, "e")
