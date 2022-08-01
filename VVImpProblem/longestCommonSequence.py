# Problem: https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    hist = dict()
    
    def lcs(self, X, Y, m, n):
        print(m, n, X[m-1], Y[n-1])
        if m == 0 or n == 0:
            return 0
        elif X[m-1] == Y[n-1]:
            if (m-1, n-1) not in self.hist:
                self.hist[(m-1, n-1)] = self.lcs(X, Y, m-1, n-1)
            return 1 + self.hist[(m-1, n-1)]
        else:
            if (m, n-1) not in self.hist:
                self.hist[(m, n-1)] = self.lcs(X, Y, m, n-1)
            if (m-1, n) not in self.hist:
                self.hist[(m-1, n)] = self.lcs(X, Y, m-1, n)
            return max(self.hist[(m, n-1)], self.hist[(m-1, n)])
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.hist = dict()
        num = self.lcs(text1 , text2, len(text1), len(text2))
        return num