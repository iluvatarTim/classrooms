# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:24:24 2017
Grahs: biconnectivity
@author: Nathalie
"""

from algopy import graph
from algopy import stack

"""
first version: returns cut point list and cut edge list
"""

def __cutpointsandedges(G, x, p, depth, cutPoints):
    
    for y in G.adjlists[x]:
        if depth[y] == -1:
            
            
            __cutpointsandedges(G, y, x, depth, cutPoints)
           
            

            
    return ph_x
    
    
def cutpointsandedges(G):
    depth = [-1] * G.order
    cutPoints = [0] * G.order
    

    for x in range(G.order):
        if depth[x] == -1:
            depth[x] = 0
            nb = 0
            for y in G.adjlists[x]:
                if depth[y] == -1:
                    
                    depth[y] = 1
                    __cutpointsandedges(G, y, x, depth, cutPoints)
                    
    
    return (cutPoints, cutEdges)
    

    
    
# result with "files/graphISP_2.gra"
    
cutPoints, cutEdges = ([1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2], 
                       [(9, 12), (13, 11), (0, 13)])
    
comp = [[(6, 5), (6, 0), (2, 6), (5, 2), (0, 5)],
  [(10, 13), (8, 3), (8, 1), (10, 8), (7, 10), (1, 7), (3, 1), (13, 3)],
  [(9, 12)],
  [(9, 11), (4, 9), (11, 4)],
  [(13, 11)],
  [(0, 13)]]  
    
    
    
