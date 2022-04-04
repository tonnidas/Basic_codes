# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    path1 = []
    path2 = []
    
    def dfs(self, root, val, decider):
        if root is None:
            return False
            
        if root.val == val:
            if decider == 1:
                self.path1.append(root.val)
            else:
                self.path2.append(root.val)
            return True
        else:
            if self.dfs(root.left, val, decider) is True or self.dfs(root.right, val, decider) is True:
                if decider == 1:
                    self.path1.append(root.val)
                else:
                    self.path2.append(root.val)
                return True
            else:
                return False
            
    def dfs2(self, root, val):
        if root is None:
            return None
        
        if root.val == val:
            return root
        
        v = self.dfs2(root.left, val)
        if v is not None:
            return v
        u = self.dfs2(root.right, val)
        if u is not None:
            return u
        else:
            return None
        
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.path1 = []
        self.path2 = []
        self.dfs(root, p.val, 1)
        self.path1.reverse()
        print(self.path1)
        self.dfs(root, q.val, 2)
        self.path2.reverse()
        print(self.path2)
    
        c = min(len(self.path1), len(self.path2))   
        lca = -1
        flag = False
        for i in range(0, c, 1):
            if self.path1[i] != self.path2[i]:
                lca = self.path1[i-1]
                flag = True
                break
                
        if flag is False:
            lca = self.path1[c-1]
                
        print(lca)
        
        return self.dfs2(root, lca)

# Input: 
# [6,2,8,0,4,7,9,null,null,3,5]
# 2
# 4