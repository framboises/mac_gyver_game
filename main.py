#! /usr/bin/env python3
# coding: utf-8
import os
from tkinter import *
import class_tool as tool
import class_character as char
from import_maze import maze

#Condition to continue the game
continue_game = True
while continue_game :

# creating the window with TKinter
    window = Tk()
    window.title("Mac Gyver: The final escape")

# creating canvas
    canvas = Canvas(window, width=600, height=600)


#Creating tool and their coords with the class Tool
    tube_tool = tool.Tool("tube")
    tube_coords, tube_coord1, tube_coord2, tk_tube_coords, tube_pic = tube_tool.coords_and_pic()
    maze[tube_coords] = str(tube_tool.name)
    tube_TK_coords = tk_tube_coords

    needle_tool = tool.Tool("needle")
    needle_coords, needle_coord1, needle_coord2, tk_needle_coords, needle_pic = needle_tool.coords_and_pic()
    maze[needle_coords] = str(needle_tool.name)
    needle_TK_coords = tk_needle_coords

    ether_tool = tool.Tool("ether")
    ether_coords, ether_coord1, ether_coord2, tk_ether_coords, ether_pic = ether_tool.coords_and_pic()
    maze[ether_coords] = str(ether_tool.name)
    ether_TK_coords = tk_ether_coords


#Creating the 2 characters and their coords with the class Character
    mac_character = char.Character("mac", True)
    mac_coords, tk_mac_coords, mac_pic = mac_character.coords_and_pic()
    mac_TK_coords = tk_mac_coords
    mac_coord1, mac_coord2 = mac_coords
    maze[mac_coords] = "mac"

    murdock_character = char.Character("murdock", False)
    murdock_coords, tk_murdock_coords, murdock_pic = murdock_character.coords_and_pic()
    murdock_TK_coords = tk_murdock_coords
    murdock_coord1, murdock_coord2 = murdock_coords
    maze[murdock_coords] = "murdock"


######################
#  Graphic elements  #
######################
# creating the maze's floor
    floor = PhotoImage(file="images/floor.gif")
    for coord_floor, value_floor in maze.items() :
        if value_floor == "free_space" or "ether" or "needle" or "tube":
            coord_x_floor, coord_y_floor = coord_floor
            canvas.create_image((coord_x_floor*40), ((coord_y_floor)*40), anchor=NW, image=floor)
        else:
            pass

# creating the walls for the maze
    wall = PhotoImage(file="images/wall.gif")
    def wall_image():
        for coord_wall, value_wall in maze.items() :
            if value_wall == "wall":
                coord_x_wall, coord_y_wall = coord_wall
                canvas.create_image((coord_x_wall*40), ((coord_y_wall)*40), anchor=NW, image=wall)
            else:
                pass
    maze_wall = wall_image()

# creating Pictures for the characters inside the canvas
    mac = canvas.create_image(mac_TK_coords,image=mac_pic)
    murdock = canvas.create_image(murdock_TK_coords,image=murdock_pic)

# creating Pictures for the tools inside the canvas
    ether = canvas.create_image(ether_TK_coords,image=ether_pic)
    needle = canvas.create_image(needle_TK_coords,image=needle_pic)
    tube = canvas.create_image(tube_TK_coords,image=tube_pic)

    
#############
#  COUNTER  #
#############    
#creating and initializing the counter
    counter = 0
# Vars for deleting the pictures'object after picking them up and count them in the counter
    needle_del = False
    tube_del = False
    ether_del = False
    murdock_del = False



#############
#KEYS EVENTS#
#############
# fonctions called when the user press the keyboard
    def keyboard_mac(event):
        global mac_move_coords, mac_TK_coords, mac_coords, maze, mac_coord1, mac_coord2, counter,\
               murdock_del, needle_del, tube_del, ether_del, continue_game, window, canvas
        touch = event.keysym
# Get back the values after the event        
        mac_coord1, mac_coord2, mac_move_coords = mac_character.deplacement(touch, mac_coord1, mac_coord2, mac_move_coords, maze)
# updating the data in the canvas      
        canvas.coords(mac, mac_move_coords[0], mac_move_coords[1])
        
        mac_coords = (mac_coord1,mac_coord2)
        
# Events when Mac is meeting Murdock with or without objects
        if mac_coords == murdock_coords and  murdock_del != True :
            if  counter >= 3 :
                murdock_del = True
                canvas.delete(murdock)
                print("Murdock is asleep, you can leave the maze. Well done Mac !")
                continue_game = False
            else :
                continue_game = True
                print("Game Over ! the guardian wasn't asleep")
                window.destroy()
            return continue_game
                
        if mac_coords == (14,13):
            window.destroy()
            return continue_game

# Events when mac gyver is picking_up the 3 objects
        if mac_coords == ether_coords and  ether_del != True:
            canvas.delete(ether)
            ether_del = True
            maze[ether_coords] = "free_space"
            counter += 1
            print("You've got the " + str(ether_tool.name)+ ". " + str(3-counter), " objects left to create a syringe")

        elif mac_coords == tube_coords and  tube_del != True:
            canvas.delete(tube)
            tube_del = True
            maze[tube_coords] = "free_space"
            counter += 1
            print("You've got the " + str(tube_tool.name)+ ". " + str(3-counter), " objects left to create a syringe")

        elif mac_coords == needle_coords and  needle_del != True:
            canvas.delete(needle)
            needle_del = True
            maze[needle_coords] = "free_space"
            counter += 1
            print("You've got the " + str(needle_tool.name)+ ". " + str(3-counter), " objects left to create a syringe")

# Events when mac gyver gather the 3 tools
        elif counter == 3 :
            print("Yheah ! combining the needle, the tube and the ether,\nyou've created a syringe to make asleep the guardian")
            counter = 4
        
# initializing first position's coords of Mac in the window        
    mac_move_coords = mac_TK_coords

# Tk fonctions when the user press the keyboard on the canvas
    canvas.focus_set()
    canvas.bind("<Key>", keyboard_mac)


    canvas.pack()
    window.mainloop()

