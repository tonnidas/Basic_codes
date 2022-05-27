Problem: https://leetcode.com/problems/longest-univalue-path/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# A short version me and dipta later came up with, but the same logic of my 1st solution
class Solution:
    glob = 0
    
    def dfs(self, root):
        if root is None:
            return 0
        
        m1 = self.dfs(root.left)
        m2 = self.dfs(root.right)
        
        mm1 = 0
        mm2 = 0
        
        if root.left and root.val == root.left.val:
            mm1 = m1 + 1
        if root.right and root.val == root.right.val:
            mm2 = m2 + 1
        
        s = mm1 + mm2
        self.glob = max(self.glob, s)
            
        return max(mm1, mm2)
         
            
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.glob = 0
        self.dfs(root)
        return self.glob

# 1st version of the solution that I alone came up with

# class Solution:
#     glob = -1
    
#     def dfs(self, root):
#         m = 0
#         s = 0
        
#         if root is None:
#             if self.glob < s:
#                 self.glob = s
#             return m, s
        
#         m1, s1 = self.dfs(root.left)
#         m2, s2 = self.dfs(root.right)
        
#         if not root.left and not root.right:
#             if self.glob < s:
#                 self.glob = s
#             return m, s
        
#         if root.left and not root.right:
#             if root.val == root.left.val:
#                 m = m1 + 1 # combining two steps: m1 = m1 + 1 /n m = m1 + 1
#                 s = m1 + 1
#                 if self.glob < max(s1, s2):
#                     self.glob = max(s1, s2)
#             else:
#                 m = 0
#                 s = max(s1, s2)
#                 if self.glob < s:
#                     self.glob = s
            
#         elif not root.left and root.right:
#             if root.val == root.right.val:
#                 m = m2 + 1 # combining two steps: m2 = m2 + 1 /n m = m2 + 1
#                 s = m2 + 1
#                 if self.glob < max(s1, s2):
#                     self.glob = max(s1, s2)
#             else:
#                 m = 0
#                 s = max(s1, s2)
#                 if self.glob < s:
#                     self.glob = s
            
#         else: # both child present
#             if root.val == root.left.val and root.val == root.right.val:
#                 m1 = m1 + 1
#                 m2 = m2 + 1
#                 m = max(m1, m2)
#                 s = m1 + m2
#                 if self.glob < s:
#                     self.glob = s
#             elif root.val == root.left.val and root.val != root.right.val:
#                 m = m1 + 1 # combining two steps: m1 = m1 + 1 /n m = m1 + 1
#                 s = m1 + 1
#                 if self.glob< max(s1, s2):
#                     self.glob = max(s1, s2)
#             elif root.val != root.left.val and root.val == root.right.val:
#                 m = m2 + 1 # combining two steps: m2 = m2 + 1 /n m = m2 + 1
#                 s = m2 + 1
#                 if self.glob<max(s1, s2):
#                     self.glob = max(s1, s2)
#             else: # root.val != root.left.val and root.val != root.right.val
#                 m = 0
#                 s = max(s1, s2)
#                 if self.glob<s:
#                     self.glob = s
                    
#         if self.glob<s:
#             self.glob = s
            
#         return m, s
         
            
#     def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
#         self.glob = -1
#         g, b = self.dfs(root)
        
#         return self.glob