#! /usr/bin/env python3
# coding: utf-8
from tkinter import PhotoImage

#Class for  Mac et Murdock
class Character:
    def __init__(self, name, can_move):
        self.name = name
        self.can_move = can_move
            

    def coords_and_pic(self):
        if self.can_move == True:
            coords = (0,1)
            TK_coords = [(0*40+20),(1*40+20)]
            photo = PhotoImage(file="images/"+str(self.name)+".png")
            return coords, TK_coords, photo
        else:
            coords = (13,13)
            TK_coords = [(13*40+20),(13*40+20)]
            photo = PhotoImage(file="images/"+str(self.name)+".png")
            return coords, TK_coords, photo

         


if __name__ == "__main__":
    pass
    


        
