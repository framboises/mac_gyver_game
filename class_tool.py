#! /usr/bin/env python3
# coding: utf-8
from random import randrange
from tkinter import PhotoImage
from import_maze import maze as maze



#Class for  the three random items
class Tool:
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




if __name__ == "__main__":
    pass
