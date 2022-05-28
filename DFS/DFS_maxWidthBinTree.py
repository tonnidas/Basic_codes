# Problem: https://leetcode.com/problems/maximum-width-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    level = 1
    ans = 1
    mini = dict()
    maxi = dict()
    
    def dfs(self, root, n, level):
        if not root:
            return
        if level not in self.mini:
            self.mini[level] = n
        self.mini[level] = min(self.mini[level], n) 
        self.maxi[level] = max(self.maxi[level], n) 
        self.ans = max(self.ans, self.maxi[level] - self.mini[level] + 1)
        self.dfs(root.left, 2*n, level+1)
        self.dfs(root.right, 2*n+1, level+1)
    
    def depth(self, root, val) -> int:
        if not root:
            return
        self.level = max(val, self.level)
        self.depth(root.left, val+1)
        self.depth(root.right, val+1)
   
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.level = 1
        self.mini = dict()
        self.maxi = dict()
        self.ans = 1
        
        self.depth(root, 1)
        
        for i in range(self.level+1):            
            self.maxi[i] = 0
            
        self.dfs(root, 1, 1)
                   
        return self.ans