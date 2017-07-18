#! /usr/bin/env python3
# coding: utf-8
import os
import csv

def parse_level(maze_file):
    directory = os.path.dirname(__file__) # we get the right path.
    path_to_file = os.path.join(directory, "level", maze_file) # with this path, we go inside the folder `data` and get the file
    with open(path_to_file,"r") as f:
        coord_x = -1 #we set the coords for each case of each sprite
        coord_y = -1 #we set the coords for each case of each sprite
        maze = {} # we create the dictionary maze
        level = csv.reader(f, delimiter=';', dialect='excel')
        for row in level:
            coord_x = -1
            coord_y = coord_y+1
            for lettre in row:
                coord_x = coord_x+1
                
                if lettre == "w":
                    case = "wall"
                    maze[(coord_x,coord_y)] = case
                else:
                    case = "free_space"                    
                    maze[(coord_x,coord_y)] = case
##        print(maze)
        return maze
maze = parse_level('maze.csv')

            
            
        





if __name__ == "__main__":
    print(maze)

    
