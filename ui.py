import tkinter as tk
from tkinter import font

from config import SYMBOL
from board import Board
from game import Game
from player import Player, Bot


class TicTacToeUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.game = None
        self.boutons = {}
        self.afficher_reglages()


    def afficher_reglages(self):
        self.vider_fenetre()
        tk.Label(self, text="Choisis ton symbole", font=font.Font(size=28, weight="bold")).pack(pady=10)

        cadre = tk.Frame(self)
        cadre.pack(pady=10)
        for symbole in SYMBOL:
            tk.Button(
                cadre,
                text=symbole,
                font=font.Font(size=28, weight="bold"),
                width=4,
                command=lambda s=symbole: self.demarrer_partie(s),
            ).pack(side=tk.LEFT, padx=5)

    def demarrer_partie(self, symbole_joueur):
        symbole_bot = SYMBOL[1] if symbole_joueur == SYMBOL[0] else SYMBOL[0]
        self.game = Game(Player(symbole_joueur), Bot(symbole_bot), Board())
        self.afficher_plateau()
        self.jouer_bot_si_besoin()


    def afficher_plateau(self):
        self.vider_fenetre()

        self.etiquette = tk.Label(
            self,
            text="A toi de jouer",
            font=font.Font(size=28, weight="bold"),
        )
        self.etiquette.pack()

        grille = tk.Frame(master=self)
        grille.pack()
        self.boutons = {}
        taille = self.game.board.taille
        for y in range(taille):
            self.rowconfigure(y, weight=1, minsize=50)
            self.columnconfigure(y, weight=1, minsize=75)
            for x in range(taille):
                bouton = tk.Button(
                    master=grille,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    bg="white",
                )
                self.boutons[(x, y)] = bouton
                bouton.bind("<ButtonPress-1>", self.on_clic)
                bouton.grid(row=y, column=x, padx=5, pady=5, sticky="nsew")

        cadre = tk.Frame(self)
        cadre.pack(pady=10)
        tk.Button(cadre, text="Rejouer", command=self.rejouer).pack(side=tk.LEFT, padx=5)
        tk.Button(cadre, text="Changer de symbole", command=self.afficher_reglages).pack(side=tk.LEFT, padx=5)
        

    def on_clic(self, event):
        x, y = self.coordonnees_du_bouton(event.widget)
        if self.game.est_au_bot():
            return
        if not self.game.jouer_tour(x, y):
            return
        self.rafraichir()
        self.jouer_bot_si_besoin()

    def coordonnees_du_bouton(self, bouton):
        for (x, y), b in self.boutons.items():
            if b == bouton:
                return x, y
        return None, None

    def jouer_bot_si_besoin(self):
        if not self.game.termine and self.game.est_au_bot():
            self.after(500, self.tour_du_bot)

    def tour_du_bot(self):
        self.game.jouer_bot()
        self.rafraichir()

    def rafraichir(self):
        for (x, y), bouton in self.boutons.items():
            symbole = self.game.board.cases[x][y]
            bouton.config(text=symbole if symbole is not None else "")
        self.etiquette.config(text=self.message_etat())
        
    def message_etat(self):
        if self.game.winner is not None:
            return f"{self.game.winner} gagne !"
        if self.game.termine:
            return "Match nul"
        return "A toi de jouer"

    def rejouer(self):
        self.game.reset()
        self.rafraichir()
        self.jouer_bot_si_besoin()

    def vider_fenetre(self):
        for widget in self.winfo_children():
            widget.destroy()