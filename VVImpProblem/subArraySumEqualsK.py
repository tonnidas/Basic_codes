# Problem: https://leetcode.com/problems/subarray-sum-equals-k/submissions/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, prefsum, d = 0, 0, dict()
        d[0] = 1
        
        for i in range(len(nums)):
            prefsum = prefsum + nums[i]
            
            if prefsum-k in d: ans = ans + d[prefsum-k]
                
            if prefsum not in d: d[prefsum] = 1
            else: d[prefsum] = d[prefsum]+1
        return ans