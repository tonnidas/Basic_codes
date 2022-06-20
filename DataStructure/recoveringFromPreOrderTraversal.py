# Problem: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dash = 0
        number = ""
        nodes = list()
        level = 0
        
        # Making a list of tuples where each tuple of the list has the number first and than no of dashes this number had before it.
        # for input: "1-401--349---90--88"
        # Output: [(1, 0), (401, 1), (349, 2), (90, 3), (88, 2)]
        # I address this output from this for loop as "nodes"
        # It's complexity is O(n)
        # Notice that each[1] in nodes is the level of each[0]'s parent
        for i in range(len(traversal)):
            if traversal[i] == "-":
                if number != "":
                    level = max(level, dash+1)
                    nodes.append((int(number), dash))
                    number = ""
                    dash = 1
                else:
                    dash = dash + 1
            else:
                number = number + traversal[i]
        if number != "":
            level = max(level, dash+1)
            nodes.append((int(number), dash))
        
        # Now I make the tree and also, a list of treenodes addressed as "stack"
        stack = [None] * (level+1)
        print(stack)
        for each in nodes:
            print(each)
            if each[1] == 0:
                root = TreeNode(each[0], None, None)
                stack[1] = root
                continue
                
            if not stack[each[1]].left:
                stack[each[1]].left = TreeNode(each[0], None, None)
                stack[each[1] + 1] = stack[each[1]].left
            else:
                stack[each[1]].right = TreeNode(each[0], None, None)
                stack[each[1] + 1] = stack[each[1]].right
                stack[each[1]] = None     
        return root

# Input: traversal = "1-401--349---90--88"
# Output: [1,401,null,349,88,90]