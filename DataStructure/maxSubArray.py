# Problem: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        check = False
        for i in range(0, len(nums)):
            # there is atleast one positive number
            if nums[i] >= 0:
                check = True
        
        # Only handles the array if it has 0 or any larger positive number
        if check == True:
            max_so_far = nums[0]
            max_ending_here = 0

            for i in range(0, len(nums)):
                max_ending_here = max_ending_here + nums[i]
                if max_ending_here < 0:
                    max_ending_here = 0

                # Do not compare for all elements. Compare only  
                # when  max_ending_here > 0
                elif (max_so_far < max_ending_here):
                    max_so_far = max_ending_here
            return max_so_far
        
        # To handle the array if all the elementsv are negative 
        else: 
            res = abs(nums[i])
            for i in range(0, len(nums)):
                res = min(abs(nums[i]), res)
            return 0-res