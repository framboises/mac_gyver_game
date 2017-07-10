#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Le labyrinthe
maze = {(0,14):"wall", (1,14):"wall", (2,14):"wall", (3,14):"wall", (4,14):"wall", (5,14):"wall", (6,14):"wall", (7,14):"wall", (8,14):"wall", (9,14):"wall", (10,14):"wall", (11,14):"wall", (12,14):"wall", (13,14):"wall", (14,14):"wall",
        (0,13):"free_space", (1,13):"free_space", (2,13):"wall", (3,13):"free_space", (4,13):"wall", (5,13):"free_space", (6,13):"free_space", (7,13):"free_space", (8,13):"wall", (9,13):"free_space", (10,13):"free_space", (11,13):"free_space", (12,13):"wall", (13,13):"free_space", (14,13):"free_space",
        (0,12):"wall", (1,12):"free_space", (2,12):"wall", (3,12):"free_space", (4,12):"wall", (5,12):"free_space", (6,12):"wall", (7,12):"wall", (8,12):"wall", (9,12):"free_space", (10,12):"wall", (11,12):"free_space", (12,12):"wall", (13,12):"free_space", (14,12):"wall",
        (0,11):"wall", (1,11):"free_space", (2,11):"free_space", (3,11):"free_space", (4,11):"free_space", (5,11):"free_space", (6,11):"free_space", (7,11):"free_space", (8,11):"free_space", (9,11):"free_space", (10,11):"wall", (11,11):"free_space", (12,11):"free_space", (13,11):"free_space", (14,11):"wall",
        (0,10):"wall", (1,10):"free_space", (2,10):"wall", (3,10):"free_space", (4,10):"wall", (5,10):"wall", (6,10):"free_space", (7,10):"wall", (8,10):"free_space", (9,10):"wall", (10,10):"free_space", (11,10):"free_space", (12,10):"wall", (13,10):"wall", (14,10):"wall",
        (0,9):"wall", (1,9):"free_space", (2,9):"wall", (3,9):"free_space", (4,9):"wall", (5,9):"free_space", (6,9):"free_space", (7,9):"wall", (8,9):"free_space", (9,9):"wall", (10,9):"free_space", (11,9):"wall", (12,9):"wall", (13,9):"free_space", (14,9):"wall",
        (0,8):"wall", (1,8):"free_space", (2,8):"wall", (3,8):"free_space", (4,8):"free_space", (5,8):"free_space", (6,8):"free_space", (7,8):"wall", (8,8):"free_space", (9,8):"wall", (10,8):"free_space", (11,8):"wall", (12,8):"free_space", (13,8):"free_space", (14,8):"wall",
        (0,7):"wall", (1,7):"wall", (2,7):"wall", (3,7):"free_space", (4,7):"wall", (5,7):"wall", (6,7):"wall", (7,7):"wall", (8,7):"wall", (9,7):"wall", (10,7):"free_space", (11,7):"wall", (12,7):"wall", (13,7):"free_space", (14,7):"wall",
        (0,6):"wall", (1,6):"free_space", (2,6):"free_space", (3,6):"free_space", (4,6):"wall", (5,6):"free_space", (6,6):"free_space", (7,6):"free_space", (8,6):"wall", (9,6):"free_space", (10,6):"free_space", (11,6):"free_space", (12,6):"wall", (13,6):"free_space", (14,6):"wall",
        (0,5):"wall", (1,5):"wall", (2,5):"free_space", (3,5):"wall", (4,5):"free_space", (5,5):"free_space", (6,5):"wall", (7,5):"free_space", (8,5):"wall", (9,5):"free_space", (10,5):"wall", (11,5):"free_space", (12,5):"free_space", (13,5):"free_space", (14,5):"wall",
        (0,4):"wall", (1,4):"free_space", (2,4):"free_space", (3,4):"free_space", (4,4):"wall", (5,4):"wall", (6,4):"wall", (7,4):"free_space", (8,4):"wall", (9,4):"wall", (10,4):"wall", (11,4):"wall", (12,4):"wall", (13,4):"free_space", (14,4):"wall",
        (0,3):"wall", (1,3):"wall", (2,3):"free_space", (3,3):"wall", (4,3):"free_space", (5,3):"free_space", (6,3):"free_space", (7,3):"free_space", (8,3):"wall", (9,3):"free_space", (10,3):"free_space", (11,3):"free_space", (12,3):"free_space", (13,3):"free_space", (14,3):"wall",
        (0,2):"wall", (1,2):"wall", (2,2):"free_space", (3,2):"wall", (4,2):"free_space", (5,2):"wall", (6,2):"free_space", (7,2):"wall", (8,2):"wall", (9,2):"free_space", (10,2):"wall", (11,2):"wall", (12,2):"wall", (13,2):"wall", (14,2):"wall",
        (0,1):"wall", (1,1):"wall", (2,1):"free_space", (3,1):"free_space", (4,1):"free_space", (5,1):"wall", (6,1):"free_space", (7,1):"free_space", (8,1):"wall", (9,1):"free_space", (10,1):"free_space", (11,1):"free_space", (12,1):"free_space", (13,1):"free_space", (14,1):"free_space",
        (0,0):"wall", (1,0):"wall", (2,0):"wall", (3,0):"wall", (4,0):"wall", (5,0):"wall", (6,0):"wall", (7,0):"wall", (8,0):"wall", (9,0):"wall", (10,0):"wall", (11,0):"wall", (12,0):"wall", (13,0):"wall", (14,0):"wall"}
