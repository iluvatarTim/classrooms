#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:15:57 2018
@author: nath
"""

from algopy import graph, queue


def __pathBFS(G, src, dst, p):
    """
    return True if dst reachable from src
    """
    q = queue.Queue()
    q.enqueue(src)
    p[s] = -1
    while not q.isempty():
        s = q.dequeue()
        for adj in G.adjlists[s]:
            if p[adj] == None:
                q.enqueue(adj)
                p[adj] = s
            
def pathBFS(G, src, dst):
    p = [None] * G.order
    path = []
    if __pathBFS(G, src, dst, p):
        # build path
    
    return path


def __pathDFS(G, src, dst, M, path):
    """
    if dst reachable:
        return True
        build path
    else return False
    """
    #FIXME
    
def pathDFS(G, src, dst):
    M = [False] * G.order
    path = []
    if __pathDFS(G, src, dst, M, path):
        # something to add?
    return path

