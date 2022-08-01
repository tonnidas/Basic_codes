# Problem: https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def isPa(self, s):
        return s == s[::-1]
    
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            for j in range(0, i+1):
                if self.isPa(s[j:i+1]) == True:
                    count = count + 1
        return count