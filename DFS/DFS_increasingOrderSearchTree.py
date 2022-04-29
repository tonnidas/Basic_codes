# Problem: https://leetcode.com/problems/increasing-order-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    finalroot = None
    parent = None
    
    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        
        if self.parent is None:
            self.finalroot = TreeNode(root.val, None, None)
            self.parent = self.finalroot
        else:
            newNode = TreeNode(root.val, None, None)
            self.parent.right = newNode
            self.parent = newNode
        
        self.inorder(root.right)
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.inorder(root)
        return self.finalroot

# Input:
# [5,3,6,2,4,null,8,1,null,null,null,7]