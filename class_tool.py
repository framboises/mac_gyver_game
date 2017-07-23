#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from random import randrange
from tkinter import PhotoImage
from import_maze import maze



#Class for  the three random items
class Tool:
    def __init__(self, name):
        self.name = name
        
            
    def get_random_position(self):
        random_position = randrange(0,14)
        return random_position
            
    def coords_and_pic(self):
        
        new_random_coords = True
        while new_random_coords:
            coords = (self.get_random_position(),self.get_random_position())
            coord1, coord2 = coords
            TK_coords = [(coord1*40+20),((coord2)*40+20)]
            
            photo = PhotoImage(file="images/"+str(self.name)+".png")
            
                                               
            if maze[coords] == "free_space" and (coord1,coord2) != (13,13) and (coord1,coord2) != (0,1) :
                new_random_coords = False
                
                
                return coords, coord1, coord2, TK_coords, photo
            else:
                pass

            



    




if __name__ == "__main__":
    pass
