from random import shuffle
from board import *
from player import Player
from occupation import Occupation
from improvement import Improvement

class Game:
    def __init__(self, numPlayers, deck):
        #players
        self.numPlayers = numPlayers # May change to more later
        self.players = []
        for x in range(numPlayers):
            self.players.append(Player())

        #occs and improvements
        self.deck = deck
        
        self.majors = []
        self.minors = []
        self.occs = []
        self.loadCards(self.deck)

        #round cards
        self.roundCards = [["1Sow/Bake", "1Sheep", "1Major", "1Fence"], ["2Reno", "2Growth", "2Stone"], ["3Boar", "3Vegetable"], ["4Cattle", "4Stone"], ["5Plow/Sow", "5Growth"], ["6Reno"]]
        self.shuffleRoundCards()

        #accumulating spaces
        self.wood = [("wood", 0)]
        self.clay = []
        self.reed = []
        self.fishing = []
        self.sheep = []
        self.boar = []
        self.cattle = []
        self.stoneR2 = []
        self.stoneR6 = []

        #effects dict
        self.effects = {}

    def loadCards(self, deck):
        for x in deck:
            if x[0].isdigit():
                # occ
                f = open(x + ".txt", "r")
                line = "start"
                while (line != ""):
                    german = f.readline()
                    english = f.readline()
                    numPlayer = f.readline()
                    deck = f.readline()
                    concise = f.readline()
                    description = f.readline()
                    line = f.readline()
                    self.occs.append(Occupation(english, concise, description))
                f.close()
            else:
                f = open(x + ".txt", "r")
                line = "start"
                while (line != ""):
                    german = f.readline()
                    english = f.readline()
                    deck = f.readline()
                    prereq = f.readline()
                    cost = f.readline()
                    vp = f.readline()
                    concise = f.readline()
                    description = f.readline()
                    line = f.readline()
                    self.minors.append(Improvement(english, prereq, cost, vp, concise, description))
                f.close()
    def shuffleRoundCards(self):
        for x in self.roundCards:
            shuffle(x)
    def dealOccs(self):
        shuffle(self.occs)
        for x in range(len(self.players)):
            self.players[x].occs.append(self.occs[x * 7:(x + 1)* 7])
    def dealMinors(self):
        shuffle(self.occs)
        for x in range(len(self.players)):
            self.players[x].minors.append(self.minors[x * 7:(x + 1)* 7])

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
        resources = [(player.wood, 0), (player.clay, 0), (player.stone, 0), (player.reed, 0)]
        #check material of player's home
        roomType = player.board[0][2].type 
        if roomType == SquareType.woodenRoom:
            resources[0][1] += 5 * numRooms
        elif roomType == SquareType.clayRoom:
            resources[1][1] += 5 * numRooms
        else:
            resources[2][1] += 5 * numRooms
        #reed cost
        resources[3][1] += 2 * numRooms
        #stable cost
        resources[0][1] += 2 * numStables
        #apply effects
        

        #check & subtract
        if checkSubtract(tupList) == 1:
            raise MyError
    def startingPlayer(self, player):
        #change starting player
        while self.players[0] != player:
            self.players.append(self.players.pop([0]))
        #play minor improvement
    #def playImprovement(self, player, improvement, major = False):
    def dayLaborer(self, player):
        player.food += 2
