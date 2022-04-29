# Problem: https://leetcode.com/problems/univalued-binary-tree/

class Solution:
    
    ans = True 
    def dfs(self, root, value):
        if root:
            if root.val != value:
                self.ans = False
                return 
            self.dfs(root.left, value)
            self.dfs(root.right, value)
        else:
            return
        
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val
        self.dfs(root, value)
        return self.ans
        

# Input: root = [1,1,1,1,1,null,1]
# Output: true