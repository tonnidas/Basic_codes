# Bottom Left most tree vale problem link: https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    a = []
    
    def DeepestLevel_leftMost(self, root, level) -> int:
        if root is None:
            return 

        if root.left is None and root.right is None:
            print("yee")
            self.a.append((level,root.val))
            
        self.DeepestLevel_leftMost(root.left, level+1)
        self.DeepestLevel_leftMost(root.right, level+1)
        
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.a = []
        self.DeepestLevel_leftMost(root, 1)
        
        n = -9999999999999999
        if len(self.a) > 0:
            n = max(self.a, key=itemgetter(0))[1]
        return n