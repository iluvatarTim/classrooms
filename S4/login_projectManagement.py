# -*- coding: utf-8 -*-
"""
S4 - April 2018
Shortest Path Homework
@author: insert your login
"""

from algopy import graph, queue

inf = float('inf')

# example: the project "Christophe's house"

myHouse = [(2, []), (7, []), (3, [0, 1]), (1, [2]), (8, [0, 1]), (2, [3, 4]),
           (1,  [3, 4]), (1, [3, 4]), (3, [6]), (2, [8]), (1, [5, 9])]
           
          

# reminder:  
#   G = graph.Graph(order, directed=True)     # a new digraph
#   G.costs = {}                              # init costs (a dictionnary)
#   G.costs[(x, y)] = val                     # add the cost of edge (x, y)

def project(L):
    """
    L: for each task t, a pair (duration, list of tasks)
    - duration: its duration (a float) !
    - list of tasks: that have to be finished before t 
    
    returns (dates, expected time):
    - dates: for each task (earliest time, slack) 
    - the minimum expected project duration
    """
    
    #FIXME
    
    return None

## example:
# project(myHouse)
#Out[2]: 
#([(0, 5),
#  (0, 0),
#  (7, 4),
#  (10, 4),
#  (7, 0),
#  (15, 4),
#  (15, 0),
#  (15, 6),
#  (16, 0),
#  (19, 0),
#  (21, 0)],
# 22)