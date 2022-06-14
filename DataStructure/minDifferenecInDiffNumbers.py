# Problem: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diff = 0
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.diff = 0
        if root.left:
            self.diff = abs(root.val - root.left.val)
        else:
            self.diff = abs(root.val - root.right.val)
        self.nodes = list()
        
        def dfs(node):
            if not node:
                return
            self.nodes.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        print(self.nodes)
        self.nodes.sort()
        for i in range(len(self.nodes)-1):
            self.diff = min(self.diff, abs(self.nodes[i] - self.nodes[i+1]))

            
        return self.diff
        