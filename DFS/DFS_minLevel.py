class Solution:
    def ss(self, root: Optional[TreeNode], c):
            
        if root.left is None and root.right is None:
            return 1+c
        elif root.left is None and root.right is not None:
            return self.ss(root.right, 1+c)
        elif root.left is not None and root.right is None:
            return self.ss(root.left, 1+c)
        else:
            return min(self.ss(root.left, 1+c), self.ss(root.right, 1+c))
        
        
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return self.ss(root, 0)

# Input: [3,9,20,null,null,15,7]