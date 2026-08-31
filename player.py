import random


class Player:
    def __init__(self,symbole):
        self.symbole = symbole

class Bot:
    def __init__(self,symbole):
        self.symbole = symbole

    def play(self,board):
        return random.choice(board.cases_vides())