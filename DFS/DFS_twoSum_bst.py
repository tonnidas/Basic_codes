# Problem: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    d = dict()
    result = False
    
    def dfs(self, root, k):
        if root:
            target = k - root.val 
            if target in self.d:
                self.result = True
                return 
            else:
                self.d[root.val] = 1
                
            self.dfs(root.left, k)
            self.dfs(root.right, k)
        else:
            return
        
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.d = dict()
        self.result = False
        self.dfs(root, k)
        return self.result

# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true