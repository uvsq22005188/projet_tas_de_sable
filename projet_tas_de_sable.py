############################
# Groupe : MI TD03
# Kaan Doyurur
# Younous Soussi
# Haled Issouf
# Tri Nghiem
# https://github.com/uvsq22005188/projet_tas_de_sable
############################
# Import des librairies

import tkinter as tk
import numpy as np

############################
# Constantes

HAUTEUR = 300
LARGEUR = 300
BG_COLOR = "white"
PAS = 100
LOW=0
HIGH=5
COLS=LARGEUR//PAS
ROWS=HAUTEUR//PAS

############################
# Variables

############################
# Fonctions

def grille_vide():
    global configuration_courante
    for x in range(0, LARGEUR, PAS):
        canvas.create_line(x, 0, x, HAUTEUR)
    for y in range(0, HAUTEUR, PAS):
        canvas.create_line(0, y, LARGEUR, y)
    canvas.delete("carré")
    configuration_courante = np.zeros((COLS, ROWS))


def code_couleur():
    global configuration_courante
    canvas.delete("carré")
    for x in range(0,  COLS):
        for y in range(0, ROWS):
            x0 = x * PAS
            y0 = y * PAS
            x1 = x * PAS + PAS
            y1 = y * PAS + PAS
            
            
            if configuration_courante[x][y] == 0:
                canvas.create_rectangle(x0, y0, x1, y1, fill="white", tags="carré")
            elif configuration_courante[x][y] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="green", tags="carré")
            elif configuration_courante[x][y] == 2:
                canvas.create_rectangle(x0, y0, x1, y1, fill="cyan", tags="carré")
            elif configuration_courante[x][y] == 3:
                canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", tags="carré")
            elif configuration_courante[x][y] > 3:
                canvas.create_rectangle(x0, y0, x1, y1, fill="red", tags="carré")

            


def initalisation_aleatoire():
    global configuration_courante
    configuration_courante = np.random.randint(LOW, HIGH, size=(COLS, ROWS))    
    code_couleur()
    print(configuration_courante)

def addition_configuration():
    pass

def soustraction_configuration():
    pass

def sauvegarder_configuration():
    pass

def stabiliser_configuration():
    global configuration_courante
    for x in range(0,  COLS):
        for y in range(0, ROWS):
            if configuration_courante[x][y] > 3:
                configuration_courante[x][y] = configuration_courante[x][y] - 4
                if x-1 >= 0:
                    configuration_courante[x-1][y] += 1
                elif x+1 <= COLS:
                    configuration_courante[x+1][y] += 1
                elif y-1 >= 0:
                    configuration_courante[x][y-1] += 1
                elif y+1 <= ROWS:
                    configuration_courante[x][y+1] += 1
            else:
                print("stable")
                #code_couleur()
    print(configuration_courante)
    return configuration_courante
########################################################
# Partie principale

############################
#Création des widgets

#Fenêtre
root = tk.Tk()
root.title("Projet tas de sable")
content = tk.Frame(root) 

#Canvas
canvas = tk.Canvas(content, height=HAUTEUR, width=LARGEUR, bg=BG_COLOR)

#Bouton
bouton_aléatoire = tk.Button(content, text="Aléatoire", command=initalisation_aleatoire)
bouton_grille_vide = tk.Button(content, text="Grille", command=grille_vide)
bouton_stabiliser = tk.Button(content, text="Stabiliser", command=stabiliser_configuration)
bouton_couleur = tk.Button(content, text="Couleur", command=code_couleur)
############################
#Placement des widgets
content.grid(column=0, row=0)
canvas.grid(column=0, row=0)
bouton_aléatoire.grid(column=0, row=2)
bouton_grille_vide.grid(column=0, row=1)
bouton_stabiliser.grid(column=0, row=3)
bouton_couleur.grid(column=0, row=4)
#Evenement

#Boucle principale
root.mainloop()
