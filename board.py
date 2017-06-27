# -*- coding: utf-8 -*-
from random import *
from tkinter import * 

fenetre = Tk()
fenetre.title("Mac Gyver: The final escape")



################
#Plateau de jeu#
################

# création du canvas
canvas = Canvas(fenetre, width=600, height=600)

# création d'une grille de repère
#line=40
#col=40
#for line in range(0,600,40):
#    canvas.create_line(line, 0, line, 600)
#    for col in range(0,600,40):
#        canvas.create_line(0, col, 600, col)

# création du sol
floor = PhotoImage(file="images/floor.gif")

square_lenght=0
square_height=0

for square_lenght in range(0,600,40):
    canvas.create_image(square_lenght, square_height, anchor=NW, image=floor)
    for square_height in range(0,600,40):
        canvas.create_image(square_lenght, square_height, anchor=NW, image=floor)
    

# création des murs du labyrinthe

#############
#personnages#
#############

# création Personnage Murdock
#murdoc = canvas.create_rectangle(560,560,600,600,fill="blue")
murdoc_pic = PhotoImage(file="images/murdoc.png")
murdoc= canvas.create_image(580,580,image=murdoc_pic)

# création Personnage Mac gyver
#gyver = canvas.create_rectangle(0,0,40,40,fill="yellow")
gyver_pic = PhotoImage(file="images/gyver.png")
gyver= canvas.create_image(20,20,image=gyver_pic)

# fonction appellée lorsque l'utilisateur presse une touche
def clavier(event):
    global coords

    touche = event.keysym

    if touche == "Up":
        if coords[1] == 20:
            coords = (coords[0], coords[1])
        elif coords[1] > 20:
            coords = (coords[0], coords[1]-40)
    elif touche == "Down":
        if coords[1] == 580:
            coords = (coords[0], coords[1])
        elif coords[1] < 580:
            coords = (coords[0], coords[1]+40)       
    elif touche == "Right":
        if coords[0] == 580:
            coords = (coords[0], coords[1])
        elif coords[0] < 580:
            coords = (coords[0]+40, coords[1])  
    elif touche == "Left":
        if coords[0] == 20:
            coords = (coords[0], coords[1])
        elif coords[0] > 20:
            coords = (coords[0]-40, coords[1])
    elif touche == "q":
        fenetre.destroy()
    # changement de coordonnées pour Mac gyver
    canvas.coords(gyver, coords[0], coords[1])

# coordonnées initiales
coords = (20, 20)


# ajout du bond sur les touches du clavier
canvas.focus_set()
canvas.bind("<Key>", clavier)

canvas.pack()


########
#objets#
########

#positionner les objets de facon aléatoire

def get_random_position():
    random_position = randrange(0,600,20)
    if random_position %40 == 0:
        return random_position+20
    else :
        return random_position
    
     

#bouteille ether
ether_pic = PhotoImage(file="images/ether.png")
ether= canvas.create_image(get_random_position(),get_random_position(),image=ether_pic)
#aiguille ether
needle_pic = PhotoImage(file="images/needle.png")
needle= canvas.create_image(get_random_position(),get_random_position(),image=needle_pic)
#tube ether
tube_pic = PhotoImage(file="images/tube.png")
tube= canvas.create_image(get_random_position(),get_random_position(),image=tube_pic)



#but du jeu brouillon 1 : atteindre Murdoc





#but du jeu final : obtenir les 3 objets et atteindre Murdoc
    #creer les 3 objets et definir une position aleatoire à chaque partie
    #ramasser les 3 objets
        # compteur/inventaire
inventaire = LabelFrame(fenetre, text="Inventaire", padx=10, pady=10)
inventaire.pack(fill="both", expand="yes")
Label(inventaire, text="Aiguille : 0 - Tube : 0 - Ether : 0 \n Appuie sur la touche Q pour quitter").pack()
fenetre.mainloop()
        #inscrire les trois objets dans le compteur
    #placer Mac gyver sur Murdock pour gagner


