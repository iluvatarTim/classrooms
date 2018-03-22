# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 19:36:20 2016

@author: Nathalie
"""

from algopy import graph


# from S3-tuto 4: with dfs

def dfsSuff(G, s, M, L):
    M[s] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
            dfsSuff(G, adj, M, L)
    L.insert(0, s)

def topologicalOrderDFS(G):
    M = [False] * G.order
    L = []
    for s in range(G.order):
        if not M[s]:
            dfsSuff(G, s, M, L)
    return L
    
    
def testTopologicalOrder(G, L):
    M = [False] * G.order
    
    for i in range(G.order-1, -1, -1):
        s = L[i]
        M[s] = True
        for adj in G.adjlists[s]:
            if not M[adj]:
                return False
    return True


# method 2: search for a vertex with all predecessors already taken

def searchNext(G, M):
    hasPred = [False] * G.order   # hasPred[s]: s has unmarked predecessors
    for s in range(G.order):
        if not M[s]:
            for adj in G.adjlists[s]:
                hasPred[adj] = True
    for s in range(G.order):
        if not M[s] and not hasPred[s]:
            return s
    return None
    
def topologicalOrder2(G):
    M = [False] * G.order        
    L = []
    for _ in range(G.order):
        x = searchNext(G, M)
        M[x] = True
        L.append(x)
    return L
        
        
# method 3: with an indegree vector

def build_ddi(G):
    # FIXME
    pass

def topologicalOrder(G):
    ddi = build_ddi(G)
    #FIXME
        
        