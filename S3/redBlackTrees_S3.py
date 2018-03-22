# -*- coding: utf-8 -*-
"""
March 2018
@author: Nathalie
"""

from algopy import btree

btree.BTree.degree = 2
 
from algopy import redblacktree as rbt


RBT_ex = rbt.RedBlackTree(13, False,
                      rbt.RedBlackTree(8, True, 
                                   rbt.RedBlackTree(1, False, None, rbt.RedBlackTree(6, True)),
                                   rbt.RedBlackTree(11, False)),
                      rbt.RedBlackTree(17, True, 
                                   rbt.RedBlackTree(15, False), 
                                    rbt.RedBlackTree(25, False, rbt.RedBlackTree(22, True), rbt.RedBlackTree(27, True))
                                    )
                    )

# ex 1.4 q2, degree = 2
s1 = "(<13,32,44>(<3>)(<18,25>)(<35,40>)(<46,49,50>))"
B1 = btree.fromlist(s1, 2)


# second in tutorial, ex 1.4 q1 degree = 2
s2 = "(<22>(<15>(<8,12>)(<18,19,20>))(<27,41>(<24,25>)(<30,35,38>)(<45,48>)))"
B2 = btree.fromlist(s2, 2)

#----------------------------- Conversions ------------------------------------                    

def redBlackFrom24tree(T):
    if T == None:
        return None
    else:
        if T.children == []:
            children = [None] * (T.nbkeys + 1)
        else:
            children = T.children
    
        B = rbt.RedBlackTree(T.keys[0], T.nbkeys > 1, 
                             redBlackFrom24tree(children[0]), 
                             redBlackFrom24tree(children[1]))
        if T.nbkeys > 1:
            B = rbt.RedBlackTree(T.keys[1], False, B, None)
            if T.nbkeys == 2:
                B.right = redBlackFrom24tree(children[2])
            else:
                B.right = rbt.RedBlackTree(T.keys[2], True, 
                                           redBlackFrom24tree(children[2]),
                                           redBlackFrom24tree(children[3]))
        return B
        

def redBlackTo24tree(B):
    if B == None:
        return None
    else:
        N = btree.BTree()

        if B.left and B.left.red:
            pass
            
        else:
            pass
        
        
    
        if B.right and B.right.red:
            pass
            
        
        else:
            pass
        
        
        
        if N.children[0] == None:
            N.children = []
        return N
        
