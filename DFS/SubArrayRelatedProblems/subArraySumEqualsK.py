# Problem: https://leetcode.com/problems/subarray-sum-equals-k/submissions/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d, sums, count = {0:1}, 0, 0
        
        for i in range(len(nums)):
            sums = sums + nums[i]
            
            # think, of array: 1, 2, 0, 0, 0, -9, 12 and k: 3
            if sums not in d: d[sums] = 1
            else: d[sums] = d[sums] + 1
                
                
            if (sums - k) in d: count = count + d[sums - k]
                
        return count