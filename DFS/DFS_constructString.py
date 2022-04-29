# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def pre(self, root):
        if root.left is None and root.right is None:
            print("1")
            return "" + str(root.val) + ""
        if root.left is not None and root.right is None:
            print("2")
            return  str(root.val) + "(" + self.pre(root.left) + ")"
        if root.left is None and root.right is not None:
            print("3")
            return str(root.val) + "()(" + self.pre(root.right) + ")"
        else:
            print("4:")
            return str(root.val) + "(" + self.pre(root.left) + ")" + "(" + self.pre(root.right) + ")"

            
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.pre(root)
        
        
# Input: [1,2,3,null,4]     