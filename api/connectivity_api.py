# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 10:44:31 2017
Connected Graphs and connected components
@author: Nathalie
"""

from algopy import graph, graphmat

# to test on large graphs
import sys
sys.setrecursionlimit(3000)


# tools
def __edgeCount(G):
    p = 0
    for L in G.adjlists:
        p += len(L)
    if not G.directed:
        p = p // 2
    return p

def __degrees(G):
    """
    returns vertices with min and max degrees
    """
    maxi, mini = 0, G.order
    for L in G.adjlists:
        maxi = max(len(L), maxi)
        mini = min(len(L), mini)
    return (mini, maxi)
    
def ccvect_to_list(k, cc):
    '''
    return the list of G's connected components: 
    each component is a list of vertices
    '''
    comp = [[] for _ in range(k)]
    for i in range(len(cc)):
        comp[cc[i]-1].append(i)
    return comp

    
#------------------------------------------------------------------------------
# not in the tutorial : seen with istree(P3)

# test: graph is connected?

def __nbVertexDFS(G, s, M):
    M[s] = True
    nb = 1
    for adj in G.adjlists[s]:
        if not M[adj]:
            nb += __nbVertexDFS(G, adj, M)
    return nb
    
def isConnected(G):
    M = [False]*G.order
    return __nbVertexDFS(G, 0, M) == G.order


# find connected components: basic...


def __components(G, s, cc, no):
    cc[s] = no
    for adj in G.adjlists[s]:
        if cc[adj] == 0:
            __components(G, adj, cc, no)

def components(G):
    '''
    return (nbc, cc)
    nbc: the number of connected components
    cc: the vector of components 
    (cc[i] is the number of the component i belongs to)
    '''
    cc = [0]*G.order
    no = 0
    for s in range(G.order):
        if cc[s] == 0:
            no += 1
            __components(G, s, cc, no)
    return (no, cc)

def makemeconnected(G):
    (k, cc) = components(G)
    x = 0
    while k != 1:
        y = x + 1
        while cc[y] == cc[x]:
            y += 1
        G.addedge(x, y)
        k -= 1
        for i in range(y+1, G.order):
            if cc[i] == cc[y]:
                cc[i] = cc[x]
        cc[y] = cc[x]


def makemeconnected2(G):
    (k, cc) = components(G)
    x = 0
    M = [False] * (k+1)
    M[cc[x]] = True
    while k != 1:
        y = x + 1
        while M[cc[y]]:
            y += 1
        G.addedge(x, y)
        M[cc[y]] = True
        k -= 1
        x = y

def makemeconnectedDFS(G):
    M = [False] * G.order
    __components(G, 0, M, True)
    x = 0
    for y in range(1, G.order):
        if not M[y]:
            __components(G, y, M, True)
            G.addedge(x, y)
            x = y
            


#------------------------------------------------------------------------------
# Indicateurs de connexité (connectivity indicators?)
# pas dans le sujet de td, peut être gardé pour le contrôle !?

def connectivity(G):
    M = [False]*G.order
    k = 0
    IC2 = 0
    for s in range(G.order):
        if not M[s]:
            k += 1
            nb = __nbVertexDFS(G, s, M)
            IC2 += nb*nb
    IC1 = (G.order - k) / (G.order-1)
    IC2 = IC2 / (G.order * G.order)
    return (IC1, IC2)

#------------------------------------------------------------------------------
# test tree 
# connected + without cycles

def __isTree(G, s, p):
    '''
    vertex are marked with parents in p
    returns (nb, tree)
    nb: number of met vertices
    tree: boolean == without cycle
    '''
    nb = 1
    for adj in G.adjlists[s]:
        if p[adj] == None:
            p[adj] = s
            (n, tree) = __isTree(G, adj, p)
            nb += n
            if not tree:
                return (nb, False)
        else:
            if adj != p[s]:
                return (nb, False)
    return (nb, True)

def isTree(G):
    p = [None] * G.order
    p[0] = -1
    (nb, tree) = __isTree(G, 0, p)
    return tree and nb == G.order


