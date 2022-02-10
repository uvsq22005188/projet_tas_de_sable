############################
# Groupe : MI TD03
# Kaan Doyurur
#
#
#
# https://github.com/uvsq22005188/projet_tas_de_sable
############################
# Import des librairies

import tkinter as tk
import random
import numpy as np

############################
# Constantes

HAUTEUR = 600
LARGEUR = 600
BG_COLOR = "white"
PAS = 10

############################
# Variables

configuration_courante = [[], []]
############################
# Fonctions

def initialisation():
    for x in range(0, LARGEUR, PAS):
        canvas.create_line(x, 0, x, HAUTEUR)
    for y in range(0, HAUTEUR, PAS):
        canvas.create_line(0, y, LARGEUR, y)

def aléatoire():
    low=0
    high=6
    cols=LARGEUR//PAS
    rows=HAUTEUR//PAS
    liste = np.random.randint(low, high, size=(rows, cols))
    print(liste)    

    for x in range(0, LARGEUR, PAS):
        canvas.create_text()

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
bouton_aléatoire = tk.Button(content, text="Aléatoire", command=initialisation)

############################
#Placement des widgets
content.grid(column=0, row=0)
canvas.grid(column=0, row=0)
bouton_aléatoire.grid(column=0, row=1)
#Evenement

#Boucle principale
root.mainloop()
