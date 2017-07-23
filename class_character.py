#! /usr/bin/env python3
# coding: utf-8
from tkinter import PhotoImage

#Class for  Mac et Murdock
class Character:
    def __init__(self, name, can_move) :
        self.name = name
        self.can_move = can_move
            

    def coords_and_pic(self):
        if self.can_move == True :
            coords = (0,1)
            TK_coords = [(0*40+20),(1*40+20)]
            photo = PhotoImage(file="images/"+str(self.name)+".png")
            return coords, TK_coords, photo
        else:
            coords = (13,13)
            TK_coords = [(13*40+20),(13*40+20)]
            photo = PhotoImage(file="images/"+str(self.name)+".png")
            return coords, TK_coords, photo
        
    def deplacement(self, key, coord_x, coord_y, TK_coords, level):
        self.key = key
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.TK_coords = TK_coords
        self.level = level

        
        if self.can_move == True :
            if self.key == "Up":
                if self.coord_y >= 0 and self.level[(self.coord_x, self.coord_y-1)] != "wall" :
                    #Mac doesn't move when is closed to the end of the frame
                    if self.TK_coords[0] == 580:
                        pass
                    elif self.TK_coords[0] < 580:
                        self.TK_coords = (self.TK_coords[0], self.TK_coords[1]-40)
                    #changing the values of the maze
                        self.level[(self.coord_x, self.coord_y)] = "free_space"
                        self.level[(self.coord_x, self.coord_y-1)] = "mac"
                        self.coord_y = self.coord_y-1
                        return self.coord_x, self.coord_y, self.TK_coords
                else :
                        return self.coord_x, self.coord_y, self.TK_coords


            elif self.key == "Down":
                if self.coord_y <= 14 and self.level[(self.coord_x, self.coord_y+1)] != "wall" :
                    #Mac doesn't move when is closed to the end of the frame
                    if self.TK_coords[0] == 0:
                        pass
                    elif self.TK_coords[0] > 0 :
                        self.TK_coords = (self.TK_coords[0], self.TK_coords[1]+40)
                    #changing the values of the maze
                        self.level[(self.coord_x, self.coord_y)] = "free_space"
                        self.level[(self.coord_x, self.coord_y+40)] = "mac"
                        self.coord_y = self.coord_y+1
                        return self.coord_x, self.coord_y, self.TK_coords
                else :
                        return self.coord_x, self.coord_y, self.TK_coords

        if self.can_move == True :
            if self.key == "Right":
                if self.coord_x <= 13 and self.level[(self.coord_x+1, self.coord_y)] != "wall" :
                    #Mac doesn't move when is closed to the end of the frame
                    if self.TK_coords[0] == 580:
                        pass
                    elif self.TK_coords[0] < 580:
                        self.TK_coords = (self.TK_coords[0]+40, self.TK_coords[1])
                    #changing the values of the maze
                        self.level[(self.coord_x, self.coord_y)] = "free_space"
                        self.level[(self.coord_x+1, self.coord_y)] = "mac"
                        self.coord_x = self.coord_x+1
                        return self.coord_x, self.coord_y, self.TK_coords
                else :
                        return self.coord_x, self.coord_y, self.TK_coords
                        

            elif self.key == "Left":
                if self.coord_x >= 0 and self.level[(self.coord_x-1, self.coord_y)] != "wall" :
                    #Mac doesn't move when is closed to the end of the frame
                    if self.TK_coords[0] == 0:
                        pass
                    elif self.TK_coords[0] > 0 :
                        self.TK_coords = (self.TK_coords[0]-40, self.TK_coords[1])
                    #changing the values of the maze
                        self.level[(self.coord_x, self.coord_y)] = "free_space"
                        self.level[(self.coord_x-1, self.coord_y)] = "mac"
                        self.coord_x = self.coord_x-1
                        return self.coord_x, self.coord_y, self.TK_coords
                else :
                        return self.coord_x, self.coord_y, self.TK_coords


if __name__ == "__main__":
    pass
    


        
