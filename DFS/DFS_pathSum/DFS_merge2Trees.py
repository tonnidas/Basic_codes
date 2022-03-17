# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:       
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        finalroot = TreeNode(None, None, None)
        if root1 is not None and root2 is not None:
            finalroot.val = root1.val + root2.val
            finalroot.left = self.mergeTrees(root1.left, root2.left)
            finalroot.right = self.mergeTrees(root1.right, root2.right)
            
        elif root1 is not None and root2 is None:
            finalroot.val = root1.val
            finalroot.left = self.mergeTrees(root1.left, None)
            finalroot.right = self.mergeTrees(root1.right, None)
            
        elif root1 is None and root2 is not None:
            finalroot.val = root2.val
            finalroot.left = self.mergeTrees(None, root2.left)
            finalroot.right = self.mergeTrees(None, root2.right)
        else:
            finalroot = None
        
        return finalroot 
        
# Input:
# [1,3,2,5]
# [2,1,3,null,4,null,7]