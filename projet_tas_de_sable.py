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

PAS = 8
HAUTEUR = 800
LARGEUR = 800
BG_COLOR = "white"
LOW=0
HIGH=4
COLS=LARGEUR//PAS
ROWS=HAUTEUR//PAS

############################
# Variables

playing = True
stable = False
############################
# Fonctions

def grille_vide():
    global configuration, configuration_temp
    
    canvas.create_rectangle(0, 0, LARGEUR , HAUTEUR, outline="black", width=PAS*2)
    
    for x in range(0, LARGEUR, PAS):
        canvas.create_line(x, 0, x, HAUTEUR)
    for y in range(0, HAUTEUR, PAS):
        canvas.create_line(0, y, LARGEUR, y)
    canvas.delete("carré")
    configuration = np.zeros((COLS, ROWS))
    configuration_temp = configuration.copy()
    code_couleur()


def animation():
    global configuration, configuration_temp, stable, playing
    
    if playing == False:
        playing = True
    
    elif stable == False and playing == True:
        iteration_configuration()
        root.after(50, animation)

    elif stable == True:
        print("Stable !")
        playing == False

def animation_stop():
    global playing
    playing = False

def iteration_configuration():
    global configuration, configuration_temp, stable
    position_max = np.transpose(np.where(configuration>=4))
    for x, y in position_max:
        avalanche(x, y)
        code_couleur()
    if len(position_max) == 0:
        stable = True
    else:
        stable = False

def configuration_stable():
    global configuration, configuration_temp
    start = time.time()
    iteration = 0
    while np.max(configuration) >= 4:
        position_max = np.transpose(np.where(configuration >= 4))
        for x, y in position_max:
            avalanche(x, y)
        iteration += 1
        if iteration % 100 == 0:
            print("Nombre iteration : {}".format(iteration))
        
    code_couleur() 
    end = time.time()
    print("Temps total: {:.3f} secondes".format(end-start))
    print("Nombre iteration : {}".format(iteration))
   

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
            x0 = x * PAS + 0.1
            y0 = y * PAS + 0.1
            x1 = x * PAS + PAS - 0.1
            y1 = y * PAS + PAS - 0.1
            
            if configuration[x][y] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", width=0, tags="carré")
            elif configuration[x][y] == 2:
                canvas.create_rectangle(x0, y0, x1, y1, fill="green", width=0, tags="carré")
            elif configuration[x][y] == 3:
                canvas.create_rectangle(x0, y0, x1, y1, fill="blue", width=0, tags="carré")
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
    configuration = np.full((ROWS, COLS), HIGH - 1)
    configuration[0] = configuration[-1] = 0
    configuration[:, 0] = configuration[:, -1] = 0
    configuration_temp = configuration.copy()
    code_couleur()

def identity():
    global configuration, configuration_temp
    
    max = np.full((ROWS, COLS), HIGH * 2 - 2)
    max[0] = max[-1] = 0
    max[:, 0] = max[:, -1] = 0
    configuration = max.copy()
    configuration_temp = configuration.copy()
    configuration_stable()
    for x in range(ROWS):
        for y in range(COLS):
            configuration[x][y] = max[x][y] - configuration[x][y]
            if configuration[x][y] < 0:
                configuration[x][y] = 0
    configuration_temp = configuration.copy()
    configuration_stable()
    code_couleur() 


def initalisation_aleatoire():
    global configuration, configuration_temp
    configuration = np.random.randint(LOW, HIGH + 1, size=(COLS, ROWS))    
    configuration[0] = configuration[-1] = 0
    configuration[:, 0] = configuration[:, -1] = 0
    configuration_temp = configuration.copy()
    code_couleur()

def addition_configuration():
    global configuration, configuration_temp
    for x in range(ROWS):
        for y in range(COLS):
            configuration[x][y] = configuration[x][y] + configuration[x][y]
    code_couleur()
    configuration_temp = configuration.copy()
    print(configuration)

def soustraction_configuration():
    global configuration, configuration_temp
    configuration_chargé = np.loadtxt('configuration_sauvegardé.txt', dtype=int)
    for x in range(ROWS):
        for y in range(COLS):
            configuration[x][y] = configuration[x][y] - configuration_chargé[x][y]
            if configuration[x][y] < 0:
                configuration[x][y] = 0
    code_couleur()
    configuration_temp = configuration.copy()

def sauvegarder_configuration():
    np.savetxt('configuration_sauvegardé.txt', configuration, fmt='%d')

def charger_configuration():
    global configuration, configuration_temp
    configuration = np.loadtxt('configuration_sauvegardé.txt', dtype=int)
    configuration_temp = configuration.copy()
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
canvas = tk.Canvas(content, width=LARGEUR, height=HAUTEUR, bd=0, highlightthickness=0, relief='flat')
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
bouton_animation = tk.Button(content, text="Animation", command=animation)
bouton_stop = tk.Button(content, text="Stop", command=animation_stop)


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
bouton_animation.grid(column=0, row=5)
bouton_stop.grid(column=0, row=6)
#Evenement

canvas.bind("<Button-1>", clique_souris)
canvas.bind("<Button-3>", clique_souris)
#Boucle principale
root.mainloop()
