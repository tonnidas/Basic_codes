# Problem: https://leetcode.com/problems/leaf-similar-trees/submissions/

class Solution:
    lst = list()
    
    def dfs(self, node1):
        if not node1:
            return
        
        if not node1.left and not node1.right:
            self.lst.append(node1.val)
            return
        else:
            self.dfs(node1.left)
            self.dfs(node1.right)
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.lst = list()
        
        self.dfs(root1)
        lst1 = self.lst
        print(lst1)
        self.lst = list()
        self.dfs(root2)
        lst2 = self.lst
        print(lst2)
        
        if len(lst1) == len(lst2):
            for i in range(len(lst1)):
                if lst1[i] != lst2[i]:
                    return False
        else:
            return False
                
        return True
  
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true