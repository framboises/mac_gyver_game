#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from maze import *
from random import *
from tkinter import * 

##################
#     CLASS      #
##################

#Class for the tube, ether and needle
class Tools:
    def __init__(self, name):
        self.name = name
            
    def get_random_position(self):
        random_position = randrange(0,14)
        return random_position
            
    def coords(self):
        new_random_coords = True
        while new_random_coords:
            coord1 = self.get_random_position()
            coord2 = self.get_random_position()
            if maze[(coord1,coord2)] == "free_space":
                new_random_coords = False
                return (coord1,coord2)
            else:
                pass
    def picture(self):
        return PhotoImage(file="images/"+str(self.name)+".png")
        

            
#Class for  Mac et Murdock
class Character:
    def __init__(self, name, can_move):
        self.name = name
        self.can_move = can_move
            

    def coords(self):
        if self.can_move == True:
            return (0,13)
        else:
            return (13,1)
    def picture(self):
        return PhotoImage(file="images/"+str(self.name)+".png")
     
#Creating the 3 tools and their coords
tube_tools = Tools("tube")
tube_coords = tube_tools.coords()
tube_coord1, tube_coord2 = tube_coords
maze[tube_coords] = str(tube_tools.name)

needle_tools = Tools("needle")
needle_coords = needle_tools.coords()
needle_coord1, needle_coord2 = needle_coords
maze[needle_coords] = str(needle_tools.name)

ether_tools = Tools("ether")
ether_coords = ether_tools.coords()
ether_coord1, ether_coord2 = ether_coords
maze[ether_coords] = str(ether_tools.name)



#Creating the 2 characters and their coords
mac_character = Character("mac", True)
mac_coords = mac_character.coords()
mac_coord1, mac_coord2 = mac_coords
maze[mac_coords] = "mac"

murdock_character = Character("murdock", False)
murdock_coords = murdock_character.coords()
murdock_coord1, murdock_coord2 = murdock_coords
maze[murdock_coords] = "murdock"



########################
#GRAPHIKS with TKinter #
########################
    
fenetre = Tk()
fenetre.title("Mac Gyver: The final escape")

# creating canvas
canvas = Canvas(fenetre, width=600, height=600)
    
# creating floor
floor = PhotoImage(file="images/floor.gif")

for coord_floor, value_floor in maze.items() :
    if value_floor == "free_space" or "ether" or "needle" or "tube":
        coord_x_floor, coord_y_floor = coord_floor
        canvas.create_image((coord_x_floor*40), ((14-coord_y_floor)*40), anchor=NW, image=floor)
    else:
        pass
    
# creating the walls for the maze
wall = PhotoImage(file="images/wall.gif")
for coord_wall, value_wall in maze.items() :
    if value_wall == "wall":
        coord_x_wall, coord_y_wall = coord_wall
        canvas.create_image((coord_x_wall*40), ((14-coord_y_wall)*40), anchor=NW, image=wall)
    else:
        pass

# creating Pictures and coords for the objects and the characters in TKinter        
tube_pic = tube_tools.picture()
tube_TK_coords = [(tube_coord1*40+20),((14-tube_coord2)*40+20)]
tube = canvas.create_image(tube_TK_coords,image=tube_pic)

needle_pic = needle_tools.picture()    
needle_TK_coords = [(needle_coord1*40+20),((14-needle_coord2)*40+20)]
needle = canvas.create_image(needle_TK_coords,image=needle_pic)
    
ether_pic = ether_tools.picture()
ether_TK_coords = [(ether_coord1*40+20),((14-ether_coord2)*40+20)]
ether = canvas.create_image(ether_TK_coords,image=ether_pic)

mac_pic = mac_character.picture()
mac_TK_coords = [(mac_coord1*40+20),((14-mac_coord2)*40+20)]
mac = canvas.create_image(mac_TK_coords,image=mac_pic)

murdock_pic = murdock_character.picture()
murdock_TK_coords = [(murdock_coord1*40+20),((14-murdock_coord2)*40+20)]
murdock = canvas.create_image(murdock_TK_coords,image=murdock_pic)

##    print(mac_TK_coords)
##    print(mac_coords)
##    print("tube est sur la case " + str(tube_coords))
##    print("needle est sur la case " + str(needle_coords))
##    print("ether est sur la case " + str(ether_coords))
##    print("Mac est sur la case " + str(mac_coords))
##    print("Murdock est sur la case " + str(murdock_coords))    



###################################
# Starting game !                 #
#                                 # 
###################################


      
continuer_partie = True
while continuer_partie:






#############
#KEYS EVENTS#
#############

# fonction called when the user press the keyboard
    def keyboard_mac(event):
        global coords, maze, mac_coord1, mac_coord2
        

        touch = event.keysym

        if touch == "Up" and mac_coord2 >= 0 and maze[(mac_coord1,mac_coord2+1)] != "wall" :
            if coords[1] == 0:
                coords = (coords[0], coords[1])
            elif coords[1] > 0:
                coords = (coords[0], coords[1]-40)
                maze[(mac_coord1,mac_coord2)] = "free_space"
                maze[(mac_coord1,mac_coord2+1)] = "mac"
                mac_coord2 = mac_coord2+1
                mac_coords = (mac_coord1,mac_coord2)
                print(maze)
                print("Mac est sur la case (" + str(mac_coord1)+ "," + str(mac_coord2)+")")
                print("Mac est sur la case TK (" + str(coords[0])+"," + str(coords[1])+")")
                print(mac_coords)     
                


        elif touch == "Down" and mac_coord2 <= 13 and maze[(mac_coord1,mac_coord2-1)] != "wall" :
            if coords[1] == 580:
                coords = (coords[0], coords[1])
            elif coords[1] < 580:
                coords = (coords[0], coords[1]+40)
                maze[(mac_coord1,mac_coord2)] = "free_space"
                maze[(mac_coord1,mac_coord2-1)] = "mac"
                mac_coord2 = mac_coord2-1
                mac_coords = (mac_coord1,mac_coord2)
                print(maze)
                print("Mac est sur la case (" + str(mac_coord1)+ "," + str(mac_coord2)+")")
                print("Mac est sur la case TK (" + str(coords[0])+"," + str(coords[1])+")")
                print(mac_coords)      
                
        elif touch == "Right" and mac_coord1 <= 13 and maze[(mac_coord1+1,mac_coord2)] != "wall" :
            if coords[0] == 580:
                coords = (coords[0], coords[1])
            elif coords[0] < 580:
                coords = (coords[0]+40, coords[1])
                maze[(mac_coord1,mac_coord2)] = "free_space"
                maze[(mac_coord1+1,mac_coord2)] = "mac"
                mac_coord1 = mac_coord1+1
                mac_coords = (mac_coord1,mac_coord2)
                print(maze)
                print("Mac est sur la case (" + str(mac_coord1)+ "," + str(mac_coord2)+")")
                print("Mac est sur la case TK (" + str(coords[0])+"," + str(coords[1])+")")
                print(mac_coords) 

        elif touch == "Left" and mac_coord1 >= 0 and maze[(mac_coord1-1,mac_coord2)] != "wall" :
            if coords[0] == 0:
                coords = (coords[0], coords[1])
            elif coords[0] > 0:
                coords = (coords[0]-40, coords[1])
                maze[(mac_coord1,mac_coord2)] = "free_space"
                maze[(mac_coord1-1,mac_coord2)] = "mac"
                mac_coord1 = mac_coord1-1
                mac_coords = (mac_coord1,mac_coord2)
                print(maze)
                print("Mac est sur la case (" + str(mac_coord1)+ "," + str(mac_coord2)+")")
                print("Mac est sur la case TK (" + str(coords[0])+"," + str(coords[1])+")")
                print(mac_coords) 


        elif touch == "q" :
            fenetre.destroy()


# changing coords for Mac gyver
        canvas.coords(mac, coords[0], coords[1])
# first position's coords
    coords = mac_TK_coords
# add moves when touching the keyboard
    canvas.focus_set()
    canvas.bind("<Key>", keyboard_mac)
    canvas.pack()

    print(maze)
    print("Mac est sur la case " + str(mac_coord1) + str(mac_coord2))
    print(mac_TK_coords)
    print(mac_coords)

    print("murdock position : "+ str(murdock_TK_coords))
    print("murdock : "+ str(murdock_coords))
    print(coords)


    
        


        
        





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




################################
##    print(maze)
##    direction = input("quelle direction ?")
##    direction = str(direction)
### deplacement avec des inputs pour l'instant
##    if direction == "r" and mac_coord2+1 <= 14 and maze[(mac_coord1,mac_coord2+1)] != "wall" :
##        maze[(mac_coord1,mac_coord2+1)] = "mac"
##        maze[(mac_coord1,mac_coord2)] = "free_space"        
##        mac_coord2 = mac_coord2+1
##        
##    elif direction == "l" and mac_coord2 !=  0 and maze[(mac_coord1,mac_coord2-1)] != "wall" :
##        maze[(mac_coord1,mac_coord2+1)] = "mac"
##        maze[(mac_coord1,mac_coord2)] = "free_space"        
##        mac_coord2 = mac_coord2-1
##        
##    elif direction == "u" and mac_coord1 !=  0 and maze[(mac_coord1-1,mac_coord2)] != "wall" :
##        maze[(mac_coord1-1,mac_coord2)] = "mac"
##        maze[(mac_coord1,mac_coord2)] = "free_space"        
##        mac_coord1 = mac_coord1-1
##
##    elif direction == "d" and mac_coord1 <= 14 and maze[(mac_coord1+1,mac_coord2)] != "wall" :
##        maze[(mac_coord1+1,mac_coord2)] = "mac"
##        maze[(mac_coord1,mac_coord2)] = "free_space"        
##        mac_coord1 = mac_coord1+1
##                
##    else:
##        print("BOOM dans le mur")
##    print("Mac est sur la case " + str(mac_coord1) + "," + str(mac_coord2))



