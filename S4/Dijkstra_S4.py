# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:49:39 2017
Graphs: Shortest Paths Dijkstra
@author: Nathalie
"""

from algopy import graph


inf = float('inf')

G = graph.loadweightedgra("files/DijkstraTuto.wgra", int)

# cost of edge x -> y
# G.costs[(x, y)]
    
def chooseMin(dist, M):
    for i in range(len(dist)):
        #FIXME
        pass
    
    return x
    
def Dijkstra(G, src):
    dist = [inf] * G.order
    dist[src] = 0
    p = [-1] * G.order    
    M = [True] * G.order
    x = src
    n = 1
    while dist[x] < inf and n < G.order:
        M[x] = False
        for y in G.adjlists[x]:
            if dist[x] + G.costs[(x, y)] < dist[y]:
                dist[y] = dist[x] + G.costs[(x, y)]
                p[y] = x
        
        x = chooseMin(dist, M)
        n += 1
        
    return (dist, p)
    


#----------------------------------------------------------------------------

