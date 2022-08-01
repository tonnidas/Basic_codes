# Problem: https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list()
        n = nums[:]
        
        def dfs(s, n):
            if len(s) == len(nums):
                if s not in res:
                    res.append(s)
                return
            for i in range(len(n)):
                a = s[:]
                a.append(n[i])
                updatedN = n[:i] + n[i+1:]
                print("up: ", updatedN)
                dfs(a, updatedN)
                
        dfs(list(), n)
        return res