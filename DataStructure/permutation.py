# Problem: https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = list()
        def dfs(s):
            if len(s) == len(nums):
                res.append(s)
            for i in range(len(nums)):
                if nums[i] not in s:
                    a = s[:]
                    a.append(nums[i])
                    dfs(a)
        dfs(list())
        return res