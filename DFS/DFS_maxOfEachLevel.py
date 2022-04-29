# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    a = {}
    
    def st(self, root, val, level):
        if not root:
            return

        if level in self.a:
            if root.val > self.a[level]:
                self.a[level] = root.val
        else:
            self.a[level] = root.val

        self.st(root.left, val, level+1)
        self.st(root.right, val, level+1)
    
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.a = {}
        self.st(root, "", 1)
        mainA = []
        for key,value in self.a.items():
            mainA.append(self.a[key])

        return mainA        