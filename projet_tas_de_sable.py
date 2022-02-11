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

HAUTEUR = 600
LARGEUR = 600
BG_COLOR = "white"
PAS = 10
LOW=0
HIGH=5
COLS=LARGEUR//PAS
ROWS=HAUTEUR//PAS

############################
# Variables


############################
# Fonctions



def initalisation_aleatoire():
    for x in range(0, LARGEUR, PAS):
        canvas.create_line(x, 0, x, HAUTEUR)
    for y in range(0, HAUTEUR, PAS):
        canvas.create_line(0, y, LARGEUR, y)
    
    liste = np.random.randint(LOW, HIGH, size=(COLS, ROWS))    

    for x in range(0,  COLS):
        for y in range(0, ROWS):
            x0 = x * PAS
            y0 = y * PAS
            x1 = x * PAS + PAS
            y1 = y * PAS + PAS
            
            if liste[x][y] == 0:
                canvas.create_rectangle(x0, y0, x1, y1, fill="white")
            elif liste[x][y] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="green")
            elif liste[x][y] == 2:
                canvas.create_rectangle(x0, y0, x1, y1, fill="cyan")
            elif liste[x][y] == 3:
                canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
            elif liste[x][y] == 4:
                canvas.create_rectangle(x0, y0, x1, y1, fill="yellow")


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

############################
#Placement des widgets
content.grid(column=0, row=0)
canvas.grid(column=0, row=0)
bouton_aléatoire.grid(column=0, row=1)
#Evenement

#Boucle principale
root.mainloop()
