# Problem: https://leetcode.com/problems/binary-tree-right-side-view/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def level(self, l, root, n, nodes):
        if not root:
            return l-1
        nodes[n] = root
        left = self.level(l+1, root.left, 2*n, nodes)
        right = self.level(l+1, root.right, 2*n+1, nodes)
        return max(left, right)
    
    def res(self, n, root, l, d):
        if not root:
            return 
        
        if d[l] < n:
            d[l] = n
            
        self.res(2*n + 1, root.right, l+1, d)
        self.res(2*n, root.left, l+1, d)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes = dict()
        l, d, result = self.level(1, root, 1, nodes), dict(), list()
        
        for i in range(1, l+1): d[i] = 2**(i-1)

        self.res(1, root, 1, d)
        
        for each in d: result.append(nodes[d[each]].val)
            
        return result