# Problem: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    a = []
    def depth(self, root, val) -> int:
        print("root.val ===== ",root.val)
        
        if len(root.children) != 0:
            for i in range(len(root.children)):
                print("Childs: ",root.children[i].val)
                v = self.depth(root.children[i], val+1)
                print("v for ", root.children[i].val, v)
        else:
            self.a.append(val)
            return val
            
    
    def maxDepth(self, root: 'Node') -> int:
        self.a = []
        if root is not None:
            v = self.depth(root, 1)
            return max(self.a)
        else:
            return 0
        
        
# Input: 
# [1,null,3,2,4,null,5,6]
# Output:
# 3