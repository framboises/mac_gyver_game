#! /usr/bin/env python3
# coding: utf-8
from tkinter import *
import os
import class_tool as tool
import class_character as char
from import_maze import maze

#Condition to continue the game
continue_game = True
while continue_game :

########################
#GRAPHICS with TKinter #
########################

# creating the window
    window = Tk()
    window.title("Mac Gyver: The final escape")

# creating canvas
    canvas = Canvas(window, width=600, height=600)
    canvas2 = Canvas(canvas, width=600, height=600)

#Creating tool and their coords
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


#Creating the 2 characters and their coords
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

# creating floor for the maze
    floor = PhotoImage(file="images/floor.gif")
    for coord_floor, value_floor in maze.items() :
        if value_floor == "free_space" or "ether" or "needle" or "tube":
            coord_x_floor, coord_y_floor = coord_floor
            canvas2.create_image((coord_x_floor*40), ((coord_y_floor)*40), anchor=NW, image=floor)
        else:
            pass

# creating the walls for the maze
    wall = PhotoImage(file="images/wall.gif")
    def wall_image():
        for coord_wall, value_wall in maze.items() :
            if value_wall == "wall":
                coord_x_wall, coord_y_wall = coord_wall
                canvas2.create_image((coord_x_wall*40), ((coord_y_wall)*40), anchor=NW, image=wall)
            else:
                pass
    maze_wall = wall_image()


# creating Pictures for the characters inside the canvas
    mac = canvas2.create_image(mac_TK_coords,image=mac_pic)
    murdock = canvas2.create_image(murdock_TK_coords,image=murdock_pic)

# creating Pictures for the tools inside the canvas
    ether = canvas2.create_image(ether_TK_coords,image=ether_pic)
    needle = canvas2.create_image(needle_TK_coords,image=needle_pic)
    tube = canvas2.create_image(tube_TK_coords,image=tube_pic)


#COUNTER 
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
    def keyboard_mac(canvas):
        global coords, maze, mac_coord1, mac_coord2, counter, murdock_del, needle_del, tube_del, ether_del, continue_game, window, canvas2
        touch = canvas.keysym
        print("mac coord1 =",mac_coord1)



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
                



    # changing coords fcontinue_gameor Mac gyver
        canvas2.coords(mac, coords[0], coords[1])
        mac_coords = (mac_coord1,mac_coord2)
        
    # Events when Mac is meeting Murdock with or without objects
        if mac_coords == murdock_coords and  murdock_del != True :
            if  counter == 3 :
                murdock_del = True
                canvas2.delete(murdock)
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
        elif mac_coords == ether_coords and  ether_del != True:
            canvas2.delete(ether)
            ether_del = True
            maze[ether_coords] = "free_space"
            
            counter += 1
            print("You've got the " + str(ether_tool.name)+ ". " + str(3-counter), " tools left to make asleep the guardian")

        elif mac_coords == tube_coords and  tube_del != True:
            canvas2.delete(tube)
            tube_del = True
            maze[tube_coords] = "free_space"
            counter += 1
            print("You've got the " + str(tube_tool.name)+ ". " + str(3-counter), " tools left to make asleep the guardian")


        elif mac_coords == needle_coords and  needle_del != True:
            canvas2.delete(needle)
            needle_del = True
            maze[needle_coords] = "free_space"
            counter += 1
            print("You've got the " + str(needle_tool.name)+ ". " + str(3-counter), " tools left to make asleep the guardian")
        
        

    
    


    # initializing first position's coords of Mac in the window
    coords = mac_TK_coords

    


        


# fonctions called when the user press the keyboard on the canvas
    canvas2.focus_set()
    canvas2.bind("<Key>", keyboard_mac)

# fonctions called when the user press the keyboard on the canvas
    canvas.pack()
    canvas2.pack()

   
            





        
        
        



        


    window.mainloop()
