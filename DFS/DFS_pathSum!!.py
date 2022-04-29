# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    finalArray = []
    
    def ss(self, root, c, n, array) -> (List[List[int]], bool):
        array.append(root.val)
        
        if root.left is None and root.right is None:
            if (root.val + c == n):
                self.finalArray.append(array)
        elif root.left is None and root.right is not None:
            self.ss(root.right, root.val+c, n, array[:])
        elif root.left is not None and root.right is None:
            self.ss(root.left, root.val+c, n, array[:])
        else:
            self.ss(root.left, root.val+c, n, array[:])
            self.ss(root.right, root.val+c, n, array[:])
            
            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.finalArray = []
        if root is None:
            return []
        self.ss(root, 0, targetSum, [])
        return self.finalArray
        
#  Input: 
# [1,2,3]
# 5