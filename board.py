import numpy

class Board():
    #  créer la grille (matrice 6 lignes et 7 colonnes)
    grille = numpy.zeros((6, 7))
    nombre_ligne=6
    nombre_colonne = 7
  # def __init__(self):
   #     self.nombre_ligne=6
    #    self.nombre_colonne=7



    # fonction pour verifier si la case est valide (vide) ou non
    def est_valide_place(colonne:int):
        return Board.grille[5][colonne] == 0

    def pions( colonne, ligne, pion):
        Board.grille[colonne][ligne] = pion

    # detecter si la ligne suivante est occupée ou non
    def ligne_suiv( colonne:int):
        for g in range(Board.nombre_ligne):
            if Board.grille[g][colonne] == 0:
                return g

    def est_gagnant( pion:int):
        # vérifier la parie horizontale pour détecter le gagnant
        for c in range(Board.nombre_colonne - 3):
            for l in range(Board.nombre_ligne):
                if Board.grille[l][c] == pion and Board.grille[l][c + 1] == pion and Board.grille[l][c + 2] == pion and Board.grille[l][c + 3] == pion:
                    return True

        # vérifier la partie verticale
        for c in range(Board.nombre_colonne):
            for l in range(Board.nombre_ligne - 3):
                if Board.grille[l][c] == pion and Board.grille[l + 1][c] == pion and Board.grille[l + 2][c] == pion and Board.grille[l + 3][c] == pion:
                    return True
        # vérifier la partie diagonale (du gauche vers droit )
        for c in range(Board.nombre_colonne - 3):
            for l in range(Board.nombre_ligne - 3):
                if Board.grille[l][c] == pion and Board.grille[l + 1][c + 1] == pion and Board.grille[l + 2][c + 2] == pion and Board.grille[l + 3][c + 3] == pion:
                    return True
        # vérifier la partie diagonale (du droit vers le gauche )
        for c in range(Board.nombre_colonne - 3):
            for l in range(3, Board.nombre_ligne):
                if Board.grille[l][c] == pion and Board.grille[l - 1][c + 1] == pion and Board.grille[l - 2][c + 2] == pion and Board.grille[l - 3][c + 3] == pion:
                    return True

    ## fonction pour afficher la matrice correctement (sans cette fonction la matrice sera afficher vers le bas)
    def afficher_grille(self):
        return numpy.flip(Board.grille)
