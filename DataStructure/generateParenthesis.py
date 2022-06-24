# Problem: https://leetcode.com/problems/generate-parentheses/

class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
        
    ans = list()    
    def generateParenthesis(self, n):
        if n == 0:
            return []
        left, right = n, n
        self.dfs(left,right, "")
        return self.ans

    def dfs(self, left, right, st):
        if left > right:
            return
        if left == 0 and right == 0:
            self.ans.append(st)
            return
        if left != 0:
            self.dfs(left-1, right, st + "(")
        if right != 0:
            self.dfs(left, right-1, st + ")")