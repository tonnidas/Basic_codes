# Problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    a = []
    
    def sum(self, root, val):
        n = val+str(root.val)
        if root.left is None and root.right is None:
            self.a.append(n)
            return 
        
        elif root.left is not None and root.right is not None:
            self.sum(root.left, n)
            self.sum(root.right, n)
            
        elif root.left is not None and root.right is None:
            self.sum(root.left, n)
            
        else:
            self.sum(root.right, n)
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.a = []
        self.sum(root, "")
        
        num = 0
        for i in self.a:
            num = num + int(i)
            
        print(self.a)
            
        return num
        