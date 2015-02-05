from enum import Enum

class SquareType(Enum):
    empty = 1
    woodenRoom = 2
    clayRoom = 3
    stoneRoom = 4
    emptyField = 5
    grainField = 6
    vegField = 7
    stable = 8
    fencedStable = 9
    pasture = 10

class Square:
    def __init__(self):
        self.type = SquareType.empty
        self.value = 0
        self.capacity = 0
        self.neighbors = []
    def changeType(self, squareType):
        self.type = squareType
    def changeValue(self, value):
        self.value = value
    def changeCapacity(self, newCap):
        self.capacity = newCap
    def addNeighbors(self, neighbors):
        self.neighbors += neighbors

class Board:
    def __init__(self):
        self.board = [[Square() for y in range(3)] for x in range(5)]
        for x in range(5):
            for y in range(3):
                for a in [-1, 1]:
                    for b in [-1, 1]:
                        try: 
                            self.board[x][y].addNeighbors([self.board[x + a][y + b]])
                        except IndexError:
                            continue
