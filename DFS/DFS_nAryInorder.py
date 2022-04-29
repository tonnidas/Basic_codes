# Problem: https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    num = []
    def pre(self, root):
        
        if root is None:
            return 
        self.num.append(root.val)
        for i in range(len(root.children)):
            self.pre(root.children[i])
        
    def preorder(self, root: 'Node') -> List[int]:
        self.num = []
        self.pre(root)   
        return self.num

# Input: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]