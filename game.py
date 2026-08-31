
from board import Board

class Game:
    def  __init__(self, joueur, bot, board = None):
        self.board = board if board is not None else Board()
        self.premier_joueur = joueur
        self.joueur_actif = joueur
        self.bot = bot
        self.joueur = joueur
        self.winner = None
        self.termine = False

    def jouer_tour(self, x, y):
        if self.termine :
            return False
        if not self.board.est_vide_case(x, y):
            return False

        
        self.board.poser_pion(x, y, self.joueur_actif.symbole)
        self.winner = self.board.symbole_gagnant()

        if self.winner is not None or self.board.est_plein():
            self.termine = True
        else:
            self.changer_joueur()

        return True

    def changer_joueur(self):
        if self.joueur_actif == self.joueur:
            self.joueur_actif = self.bot
        else:
            self.joueur_actif = self.joueur

    def reset(self):
        self.board.reset()
        self.joueur_actif = self.joueur
        self.winner = None
        self.termine = False

