#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from tkinter import *
import os
import class_tool as tool
import class_character as char
from import_maze import maze

#####################
#TO DO : VIRTUAL ENV#
#####################





#Creating the 3 tools and their coords
tube_tool = tool.Tool("tube")
tube_coords = tube_tool.coords()
tube_coord1, tube_coord2 = tube_coords
maze[tube_coords] = str(tube_tool.name)

needle_tool = tool.Tool("needle")
needle_coords = needle_tool.coords()
needle_coord1, needle_coord2 = needle_coords
maze[needle_coords] = str(needle_tool.name)

ether_tool = tool.Tool("ether")
ether_coords = ether_tool.coords()
ether_coord1, ether_coord2 = ether_coords
maze[ether_coords] = str(ether_tool.name)



#Creating the 2 characters and their coords
mac_character = char.Character("mac", True)
mac_coords = mac_character.coords()
mac_coord1, mac_coord2 = mac_coords
maze[mac_coords] = "mac"

murdock_character = char.Character("murdock", False)
murdock_coords = murdock_character.coords()
murdock_coord1, murdock_coord2 = murdock_coords
maze[murdock_coords] = "murdock"



########################
#GRAPHICS with TKinter #
########################
# creating the window
fenetre = Tk()
fenetre.title("Mac Gyver: The final escape")

# creating canvas
canvas = Canvas(fenetre, width=600, height=600)

# creating floor's texture
floor = PhotoImage(file="images/floor.gif")

for coord_floor, value_floor in maze.items() :
    if value_floor == "free_space" or "ether" or "needle" or "tube":
        coord_x_floor, coord_y_floor = coord_floor
        canvas.create_image((coord_x_floor*40), ((coord_y_floor)*40), anchor=NW, image=floor)
    else:
        pass

# creating the walls texture for the maze
wall = PhotoImage(file="images/wall.gif")
for coord_wall, value_wall in maze.items() :
    if value_wall == "wall":
        coord_x_wall, coord_y_wall = coord_wall
        canvas.create_image((coord_x_wall*40), ((coord_y_wall)*40), anchor=NW, image=wall)
    else:
        pass

# creating Pictures and coords for the objects and the characters in TKinter
tube_pic = tube_tool.picture()
tube_TK_coords = [(tube_coord1*40+20),((tube_coord2)*40+20)]
tube = canvas.create_image(tube_TK_coords,image=tube_pic)

needle_pic = needle_tool.picture()
needle_TK_coords = [(needle_coord1*40+20),((needle_coord2)*40+20)]
needle = canvas.create_image(needle_TK_coords,image=needle_pic)

ether_pic = ether_tool.picture()
ether_TK_coords = [(ether_coord1*40+20),((ether_coord2)*40+20)]
ether = canvas.create_image(ether_TK_coords,image=ether_pic)

mac_pic = mac_character.picture()
mac_TK_coords = [(mac_coord1*40+20),((mac_coord2)*40+20)]
mac = canvas.create_image(mac_TK_coords,image=mac_pic)

murdock_pic = murdock_character.picture()
murdock_TK_coords = [(murdock_coord1*40+20),((murdock_coord2)*40+20)]
murdock = canvas.create_image(murdock_TK_coords,image=murdock_pic)



##########
#COUNTER #
##########

#creating and initializing the counter
counter = 0
# Vars for deleting the pictures'object after picking them up and count them in the counter
needle_del = False
tube_del = False
ether_del = False



###################################
# Starting game !                 #
###################################

#TO DO : Creer une condition while avec continue_game
continue_game = True




#############
#KEYS EVENTS#
#############

# fonctions called when the user press the keyboard
def keyboard_mac(event):
    global coords, maze, mac_coord1, mac_coord2, counter, needle_del, tube_del, ether_del, continue_game
    touch = event.keysym

#Conditions when "UP" is pressed
    if touch == "Up" and mac_coord2 >= 0 and maze[(mac_coord1,mac_coord2-1)] != "wall" :
        #Mac doesn't move when is closed to the end of the frame
        if coords[1] == 580:
            coords = (coords[0], coords[1])
        elif coords[1] < 580:
            coords = (coords[0], coords[1]-40)
            #changing the values of the maze
            maze[(mac_coord1,mac_coord2)] = "free_space"
            maze[(mac_coord1,mac_coord2-1)] = "mac"
            mac_coord2 = mac_coord2-1


#Conditions when "DOWN" is pressed
    elif touch == "Down" and mac_coord2 <= 14 and maze[(mac_coord1,mac_coord2+1)] != "wall" :
#Mac doesn't move when is closed to the end of the frame
        if coords[1] == 0:
            coords = (coords[0], coords[1])
        elif coords[1] > 0:
            coords = (coords[0], coords[1]+40)
            #changing the values of the maze
            maze[(mac_coord1,mac_coord2)] = "free_space"
            maze[(mac_coord1,mac_coord2+1)] = "mac"
            mac_coord2 = mac_coord2+1

#Conditions when "RIGHT" is pressed
    elif touch == "Right" and mac_coord1 <= 13 and maze[(mac_coord1+1,mac_coord2)] != "wall" :
        #Mac doesn't move when is closed to the end of the frame
        if coords[0] == 580:
            coords = (coords[0], coords[1])
        elif coords[0] < 580:
            coords = (coords[0]+40, coords[1])
            #changing the values of the maze
            maze[(mac_coord1,mac_coord2)] = "free_space"
            maze[(mac_coord1+1,mac_coord2)] = "mac"
            mac_coord1 = mac_coord1+1

#Conditions when "LEFT" is pressed
    elif touch == "Left" and mac_coord1 >= 0 and maze[(mac_coord1-1,mac_coord2)] != "wall" :
        #Mac doesn't move when is closed to the end of the frame
        if coords[0] == 0:
            coords = (coords[0], coords[1])
        elif coords[0] > 0:
            coords = (coords[0]-40, coords[1])
            #changing the values of the maze
            maze[(mac_coord1,mac_coord2)] = "free_space"
            maze[(mac_coord1-1,mac_coord2)] = "mac"
            mac_coord1 = mac_coord1-1



# changing coords for Mac gyver
    canvas.coords(mac, coords[0], coords[1])
    mac_coords = (mac_coord1,mac_coord2)
    
# Events when Mac is meeting Murdock with or without objects
    if mac_coords == murdock_coords :
        if  counter == 3 :
            continue_game = False

        else :
            fenetre.destroy()


# Events when mac gyver is picking_up the 3 objects
    elif mac_coords == ether_coords and  ether_del != True:
        canvas.delete(ether)
        ether_del = True
        counter = counter+1

    elif mac_coords == tube_coords and  tube_del != True:
        canvas.delete(tube)
        tube_del = True
        counter = counter+1


    elif mac_coords == needle_coords and  needle_del != True:
        canvas.delete(needle)
        needle_del = True
        counter = counter+1



# initializing first position's coords of Mac in the window
coords = mac_TK_coords

# add moves when touching the keyboard
canvas.focus_set()
canvas.bind("<Key>", keyboard_mac)
canvas.pack()
fenetre.mainloop()






##inventaire = LabelFrame(fenetre, text="Inventaire", padx=10, pady=10)
##inventaire.pack(fill="both", expand="yes")
##Label(inventaire, text="Aiguille : 0 - Tube : 0 - Ether : 0 \n Appuie sur la touche Q pour quitter").pack()

#
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



