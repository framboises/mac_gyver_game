#! /usr/bin/env python3
# coding: utf-8
from tkinter import PhotoImage

#Class for  Mac et Murdock
class Character:
    def __init__(self, name, can_move):
        self.name = name
        self.can_move = can_move
            

    def coords(self):
        if self.can_move == True:
            return (0,1)
        else:
            return (13,13)
    def picture(self):
        return PhotoImage(file="images/"+str(self.name)+".png")
         


if __name__ == "__main__":
    pass
    


        
