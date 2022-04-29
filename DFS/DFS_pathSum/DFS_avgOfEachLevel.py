# Problem: https://leetcode.com/problems/average-of-levels-in-binary-tree/

class Solution:
    
    a = {}
    def st(self, root, val, level):
        if not root:
            return

        if level in self.a:
            self.a[level].add(root.val)
        else:
            self.a[level] = {root.val}

        self.st(root.left, val, level+1)
        self.st(root.right, val, level+1)
    
    # def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.a = {}
        self.st(root, "", 1)
        mainA = []
        for key,value in self.a.items():
            print("self.a[", key, "] = ", self.a[key], "sum = ", sum(self.a[key]))
            mainA.append(sum(self.a[key]) / len(self.a[key]))

        return mainA

# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].