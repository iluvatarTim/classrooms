#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
April 2018
S3#
"""

from algopy import graph, graphmat, queue

def degrees(G):
    Din = [0] * G.order
    Dout = [0] * G.order
    for s in range(G.order):
        Dout[s] = len(G.adjlists[s])
        for adj in G.adjlists[s]:
            Din[adj] += 1
    
    return (Din, Dout)

def degreesMat(G):
    (din, dout) = (0, 0)
    for s in range(G.order):
        din_s, dout_s = 0, 0
        for adj in range(G.order):
            dout_s += G.adj[s][adj]
            din_s += G.adj[adj][s]
        din = max(din, din_s)
        dout = max(dout, dout_s)
    
    return (din, dout)



def __BFS(G, s, p):
    q = queue.Queue()
    q.enqueue(s)
    p[s] = -1
    while not q.isempty():
        s = q.dequeue()
        print(s)
        for adj in G.adjlists[s]:
            if p[adj] == None:
                q.enqueue(adj)
                p[adj] = s

def BFS(G):
    p = [None] * G.order
    for s in range(G.order):
        if p[s] is None:
            __BFS(G, s, p)
    return p


def __DFS(G, s, M):
    M[s] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
            __DFS(G, adj, M)

def DFS(G):
    M = [False] * G.order
    for s in range(G.order):
        if not M[s]:
            __DFS(G, s, M)

