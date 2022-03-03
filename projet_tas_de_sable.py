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
import time

############################
# Constantes

PAS = 5
HAUTEUR = 500 + PAS
LARGEUR = 500 + PAS
BG_COLOR = "white"
LOW=0
HIGH=4
COLS=LARGEUR//PAS
ROWS=HAUTEUR//PAS

############################
# Variables


############################
# Fonctions

def grille_vide():
    global configuration, configuration_temp
    for x in range(0, LARGEUR, PAS):
        canvas.create_line(x, 0, x, HAUTEUR)
    for y in range(0, HAUTEUR, PAS):
        canvas.create_line(0, y, LARGEUR, y)
    canvas.delete("carré")
    configuration = np.zeros((COLS, ROWS))
    configuration_temp = configuration.copy()

def iteration_configuration():
    global configuration, configuration_temp
    start = time.time()
    position_max = np.transpose(np.where(configuration>=4))
    for x, y in position_max:
        avalanche(x, y)
        code_couleur()
    end = time.time()
    print(end-start)

def configuration_stable():
    global configuration, configuration_temp
    start = time.time()
    while np.max(configuration) >= 4:
        x, y = np.nonzero(configuration >= 4)
        x, y = x[0], y[0]
        avalanche(x, y)
        
    code_couleur() 
    end = time.time()
    print(end-start)

def avalanche(x, y):
    global configuration, configuration_temp
    
    
    configuration_temp[x-1][y] += 1
    configuration_temp[x+1][y] += 1
    configuration_temp[x][y-1] += 1
    configuration_temp[x][y+1] += 1

    configuration_temp[0] = configuration_temp[-1] = 0
    configuration_temp[:, 0] = configuration_temp[:, -1] = 0

    configuration[x][y] -= 4
    configuration_temp[x][y] -= 4
    configuration = configuration_temp.copy()

def code_couleur():
    global configuration
    canvas.delete("carré")
    position_couleur = np.transpose(np.where(configuration>0))
    for x,y in position_couleur:
            x0 = x * PAS
            y0 = y * PAS
            x1 = x * PAS + PAS
            y1 = y * PAS + PAS
            
            if configuration[x][y] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="green", width=0, tags="carré")
            elif configuration[x][y] == 2:
                canvas.create_rectangle(x0, y0, x1, y1, fill="blue", width=0, tags="carré")
            elif configuration[x][y] == 3:
                canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", width=0, tags="carré")
            elif configuration[x][y] > 3:
                canvas.create_rectangle(x0, y0, x1, y1, fill="red", width=0, tags="carré")

def pile_centré():
    global configuration, configuration_temp
    N = entry.get()
    configuration[COLS//2][ROWS//2] = N
    configuration_temp = configuration.copy()
    code_couleur()

def max_stable():
    global configuration, configuration_temp
    configuration = np.full((ROWS, COLS), HIGH)
    configuration_temp = configuration.copy()
    code_couleur()

def identity():
    pass

def initalisation_aleatoire():
    global configuration, configuration_temp
    configuration = np.random.randint(LOW, HIGH, size=(COLS, ROWS))    
    configuration_temp = configuration.copy()
    code_couleur()

def addition_configuration():
    global configuration, configuration_temp
    for x in range(ROWS):
        for y in range(COLS):
            configuration[x][y] = configuration[x][y] + configuration[x][y]
    code_couleur()

def soustraction_configuration():
    global configuration, configuration_temp
    configuration_chargé = np.loadtxt('configuration_sauvegardé.txt', dtype=int)
    for x in range(ROWS):
        for y in range(COLS):
            configuration[x][y] = configuration[x][y] - configuration_chargé[x][y]
            if configuration[x][y] < 0:
                configuration[x][y] = 0
    code_couleur()

def sauvegarder_configuration():
    np.savetxt('configuration_sauvegardé.txt', configuration, fmt='%d')

def charger_configuration():
    global configuration
    configuration = np.loadtxt('configuration_sauvegardé.txt', dtype=int)
    code_couleur()

def clique_souris(event):
    global configuration, configuration_temp
    x = event.x // PAS
    y = event.y // PAS
    if event.num == 1:
        configuration[x][y] += 1
    elif event.num == 3:
        configuration[x][y] += 4
    configuration_temp = configuration.copy()
    code_couleur()




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
grille_vide()

#Bouton
bouton_aléatoire = tk.Button(content, text="Random", command=initalisation_aleatoire)
bouton_pile_centré = tk.Button(content, text="Pile Centré", command=pile_centré)
bouton_max_stable = tk.Button(content, text="Max Stable", command=max_stable)
bouton_identity = tk.Button(content, text="Identity", command=identity)
bouton_stabiliser = tk.Button(content, text="Itération", command=iteration_configuration)
bouton_addition = tk.Button(content, text="Addition", command=addition_configuration)
bouton_soustraction = tk.Button(content, text="Soustraction", command=soustraction_configuration)
bouton_stable = tk.Button(content, text="Stable", command=configuration_stable)
bouton_sauvegarder = tk.Button(content, text="Sauvegarder", command=sauvegarder_configuration)
bouton_charger = tk.Button(content, text="Charger", command=charger_configuration)


entry = tk.Entry(content)


############################
#Placement des widgets
content.grid(column=0, row=0)
canvas.grid(column=1, row=2)
bouton_aléatoire.grid(column=1, row=7)
bouton_stabiliser.grid(column=0, row=3)
bouton_addition.grid(column=2, row=0)
bouton_soustraction.grid(column=2, row=1)
bouton_stable.grid(column=0, row=4)
bouton_sauvegarder.grid(column=0, row=0)
bouton_charger.grid(column=0, row=1)
bouton_pile_centré.grid(column=1, row=6)
bouton_max_stable.grid(column=1, row=3)
bouton_identity.grid(column=1, row=4)
entry.grid(column=1, row=5)
#Evenement

canvas.bind("<Button-1>", clique_souris)
canvas.bind("<Button-3>", clique_souris)
#Boucle principale
root.mainloop()
