from config import TAILLE, NB, SYMBOL, CASE_VIDE



class Board:
    def __init__(self,taille=TAILLE,alignement=NB):
        self.taille = taille
        self.alignement = alignement
        self.cases = [[CASE_VIDE] * taille for _ in range(taille)]

        self.combinations = []
        self.generer_combinations()


    def generer_combinations(self):
        # horizontales
        for y in range(self.taille):
            for x in range(self.taille - self.alignement + 1):
                self.combinations.append([(x + i, y) for i in range(self.alignement)])

        # verticales
        for x in range(self.taille):
            for y in range(self.taille - self.alignement + 1):
                self.combinations.append([(x, y + i) for i in range(self.alignement)])

        # haut-gauche à bas-droite
        for x in range(self.taille - self.alignement + 1):
            for y in range(self.taille - self.alignement + 1):
                self.combinations.append([(x + i, y + i) for i in range(self.alignement)])

        # haut-droite à bas-gauche
        for x in range(self.alignement - 1, self.taille):
            for y in range(self.taille - self.alignement + 1):
                self.combinations.append([(x - i, y + i) for i in range(self.alignement)])

    def poser_pion(self, x, y, symbol):
        if self.cases[x][y] is not CASE_VIDE:
            raise ValueError("Case occupée")
        self.cases[x][y] = symbol

    def symbole_gagnant(self):
        for combinaison in self.combinations:
            symboles = [self.cases[x][y] for x, y in combinaison]
            premier = symboles[0]
            if premier is CASE_VIDE:
                continue

            tous_identiques = all(symbole == premier for symbole in symboles)
            if tous_identiques:
                return premier
        return None


    def est_vide(self, x, y):
        return self.cases[x][y] is CASE_VIDE

    def reset(self):
        for x in range(self.taille):
            for y in range(self.taille):
                self.cases[x][y] = CASE_VIDE


    # Pour le bot
    def cases_vides(self):
        cases = []
        for x in range(self.taille):
            for y in range(self.taille):
                if self.cases[x][y] is CASE_VIDE:
                    cases.append((x, y))
        return cases