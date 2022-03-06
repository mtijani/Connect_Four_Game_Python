from board import Board
import pygame
import sys
import math
###############################################
pygame.display.set_caption('Jeu de puissance 4**')
###############################################
class Interface:
    def ecrire_grille(grille:Board):
        for c in range(Board.nombre_colonne):
            for l in range(Board.nombre_ligne):
                pygame.draw.rect(screen, bleu, (c * taille, l * taille + taille, taille, taille))
                pygame.draw.circle(screen, purple, (c * taille + taille / 2, l * taille + taille + taille / 2),
                                   radius=int(taille / 2 - 6))

        for c in range(Board.nombre_colonne):
            for l in range(Board.nombre_ligne):
                if Board.grille[l][c] == 1:
                    pygame.draw.circle(screen, black, (c * taille + taille / 2, hauteur - (l * taille + taille / 2)),
                                       radius=int(taille / 2 - 6))
                elif Board.grille[l][c] == 2:
                    pygame.draw.circle(screen, white, (c * taille + taille / 2, hauteur - (l * taille + taille / 2)),
                                       radius=int(taille / 2 - 6))

        pygame.display.update()


###########################################
bleu = (0,0,70)
purple = (181,126,202)
black =(0,0,0)
white=(255,255,255)
red = (255,0,0)

grille = Board()

game_over = False
tour = 0
################################################################################################


################################################################################################
if __name__ == "__main__":
    pygame.init()
    taille = 80
    largeur = Board.nombre_ligne * taille
    hauteur = Board.nombre_colonne * taille
    size = (hauteur, hauteur)
    screen = pygame.display.set_mode(size)
    Interface.ecrire_grille(grille)

    font = pygame.font.SysFont("monospace", 50)
    while not game_over:
     for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()
        if ev.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, bleu, (0, 0, largeur+taille, taille))
            pos =ev.pos[0]
            if tour == 0:
                pygame.draw.circle(screen,black, (pos,int(taille/2)),radius=int(taille/2 -6))
            else: pygame.draw.circle(screen,white, (pos,int(taille/2)),radius=int(taille/2 -6))
        pygame.display.update()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            print(ev.pos)
            if tour == 0:
                pos=ev.pos[0]
                colonne=int(math.floor(pos/taille))

                # c'est le joueur 1 qui va commencer
              #  colonne = int(input("Joueur n°1 choisir un nombre entre 0 et 6 :"))
               # print(colonne)
                if Board.est_valide_place(colonne):
                    ligne =Board.ligne_suiv(colonne)
                    Board.pions(ligne, colonne, 1)

                if Board.est_gagnant(1):
                    # print("Le joueur 1 a gagné ")
                    f = font.render("Joueur 1 a gagné", True, red)
                    screen.blit(f,(10,10))
                    game_over = True

                tour = tour + 1

            else:
                pos = ev.pos[0]
                colonne = int(math.floor(pos / taille))

                if Board.est_valide_place(colonne):
                    ligne = Board.ligne_suiv(colonne)
                    Board.pions( ligne, colonne, 2)
                if Board.est_gagnant( 2):
                    f = font.render("Joueur 2 a gagné", True, red)
                    screen.blit(f, (10, 10))
                    game_over = True
                tour = tour - 1

            print(Board.afficher_grille(grille))
            Interface.ecrire_grille(grille)
        if game_over:
            pygame.time.wait(9000)