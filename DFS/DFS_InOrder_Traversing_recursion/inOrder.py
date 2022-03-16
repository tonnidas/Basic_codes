# Problem Reference: https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import Optional, List
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        if root is None:
            return ans

        l = self.inorderTraversal(root.left)
        ans = ans + l
            
        ans.append(root.val)
        
        r = self.inorderTraversal(root.right)
        ans = ans + r
                
        return ans

# build tree from leetcode input: https://leetcode.com/discuss/general-discussion/638847/tree-builder-for-debugging-locally
def build_tree(leet_code_input: str, should_print_tree_code_to_console=False):
    leet_code_input = leet_code_input[1:-1].split(',')
    if len(leet_code_input) == 0:
        return
    nodes = [('root', leet_code_input[0])]

    print(nodes, nodes[0][1])
    print("Tonni: ",enumerate(leet_code_input[1:]),leet_code_input[1:])

    for index, current_node in enumerate(leet_code_input[1:]):
        print("For myself : ")
        print("index: ",index,"current_node",current_node)
        print("index: ",index,"index & 1 = ",(index & 1))
        if current_node != 'null':

            if (index % 2)==1:
                print("_____ = ", nodes[index // 2][0])
                # (17 // 3) = 5 # floor division
                nodes.append((nodes[index // 2][0] + '.right', current_node)) 
            else:
                nodes.append((nodes[index // 2][0] + '.left', current_node))


    print(nodes)
    root = TreeNode(int(nodes[0][1]))


    for node in nodes:
        execution_statement: str = node[0] + ' = TreeNode(' + node[1] + ')'
        print("execution: ", execution_statement)
        if should_print_tree_code_to_console:
            print("execution: ", execution_statement)
        exec(execution_statement)
    return root


# driver
input = "[1,null,2,3]"
root = build_tree(input)
print(Solution().inorderTraversal(root))