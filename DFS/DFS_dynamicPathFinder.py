# Problem: https://leetcode.com/problems/linked-list-in-binary-tree/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    found = False
    path = dict()
    level = 1
    histry = set()
    
    def depth(self, root, val) -> int:
        if not root:
            return
        self.level = max(val, self.level)
        self.depth(root.left, val+1)
        self.depth(root.right, val+1)
    
    def dfs(self, root, n, h, pos):
        if self.found == True:
            return
        
        if n > len(self.path):
            self.found = True 
            return
            
        key = (pos, n)
        if key in self.histry:
            return
        else:
            self.histry.add(key)
            
        if not root or self.level-h < len(self.path)-n:
            return
        
        if root.val == self.path[n]:
            self.dfs(root.left, n+1, h+1, 2*pos)
            self.dfs(root.right, n+1, h+1, 2*pos+1)
        else:
            self.dfs(root.left, 1, h+1, 2*pos)
            self.dfs(root.right, 1, h+1, 2*pos+1)
            
        if root.val == self.path[1]:
            self.dfs(root.left, 2, h+1, 2*pos)
            self.dfs(root.right, 2, h+1, 2*pos+1)
        
        
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        self.found = False
        self.path = dict()
        self.level = 1
        self.histry = set()
        
        node = head
        i = 1
        while(node is not None):
            self.path[i] = node.val
            node = node.next
            i = i + 1
        
        self.depth(root, 1)
        self.dfs(root, 1, 1, 1)
        
        return self.found