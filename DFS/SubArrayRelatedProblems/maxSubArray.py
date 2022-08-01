# Problem: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        flag = "all"
        for each in nums:
            if each >= 0:
                flag = "not_all"
                
        maxim = 0
        if flag == "all":
            maxim = nums[0]
            for each in nums:
                maxim = max(each, maxim)
        else:
            print("d")
            maxim = -1
            temp = 0
            for i in range(len(nums)):
                temp = temp + nums[i]
                if temp < 0: temp = 0
                else: maxim = max(maxim, temp)
        return maxim