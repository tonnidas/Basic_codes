# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ss(self, root: Optional[TreeNode], c, n):
            
        if root.left is None and root.right is None:
            if (root.val + c == n):
                return True
            else:
                return False
            
        elif root.left is None and root.right is not None:
            return self.ss(root.right, root.val+c, n)
        elif root.left is not None and root.right is None:
            return self.ss(root.left, root.val+c, n)
        else:
            return self.ss(root.left, root.val+c, n) or self.ss(root.right, root.val+c, n)
            
    
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        else:
            return self.ss(root, 0, targetSum)


# Input : [5,4,8,11,null,13,4,7,2,null,null,null,1]
#         22
        