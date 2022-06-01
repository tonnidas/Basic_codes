# Problem: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/ 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxProduct = 0
    nodeval = []
    
    def dfs(self, root):
        if not root:
            return 0
        
        sum = root.val + self.dfs(root.left) + self.dfs(root.right)
        self.nodeval.append(sum)
        
        return sum
        
    def result(self, total):
        for v in self.nodeval:
            boro = v
            choto = total - v
            prod = boro * choto
            
            self.maxProduct = max(self.maxProduct, prod)
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.maxProduct = 0
        self.nodeval = []
        
        total = self.dfs(root)
        self.result(total)
        
        return self.maxProduct % (1000000007)
        
# Input: [1,2,3,4,5,6]
# Output: 110