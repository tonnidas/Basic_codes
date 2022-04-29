# Problem: https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    num = []
    def post(self, root):    
        if root is None:
            return
        
        for i in range(len(root.children)):
            self.post(root.children[i])
        self.num.append(root.val)
    
    def postorder(self, root: 'Node') -> List[int]:
        self.num = []
        self.post(root)
        return self.num
        
        
        