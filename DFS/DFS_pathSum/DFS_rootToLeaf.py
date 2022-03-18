# Problem: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    num = []

    def sum(self, root, value):
        value = value + str(root.val)
        
        if root.left is not None and root.right is None:
            self.sum(root.left, value)
            
        elif root.left is None and root.right is not None:
            self.sum(root.right, value)
            
        elif root.left is not None and root.right is not None:
            self.sum(root.left, value)
            self.sum(root.right, value)
            
        else:
            self.num.append(int(value, 2))
            
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.num = []
        self.sum(root, "")
        
        s = 0
        for i in self.num:
            s = s + i
            
        return s


# Input: 
# [1,0,1,0,1,0,1]

        