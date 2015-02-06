from board import *

class Player:
    def __init__(self):
        self.wood = 0
        self.clay = 0
        self.reed = 0
        self.stone = 0
        self.food = 0
        self.sheep = 0
        self.boar = 0
        self.cattle = 0
        self.grain = 0
        self.vegetable = 0
        self.points = 0
        self.person = 2
        self.availStable = 4
        self.availFences = 15 
        self.board = Board()
