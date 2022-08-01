# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/submissions/

class Solution:
    c = 0
    
    def dfs(self, root):
        if not root:
            return 0, 0
        
        n, s = self.dfs(root.left)
        n1, s1 = self.dfs(root.right)
            
        totalNodes = n + n1 + 1
        totalSum = s + s1 + root.val
        
        if totalSum // totalNodes == root.val: 
            self.c = self.c + 1
            
        print(root.val, totalNodes, totalSum, totalSum / totalNodes)
        return totalNodes, totalSum
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        
        return self.c