# Problem: https://leetcode.com/problems/subsets/

class Solution:
    
    def subsets(self, nums):
        nums.sort()
        
        # print([1,2] + []) = [1, 2]
        
        result = [[]]
        print("result = ", result)
        for num in nums:
            r = [i + [num] for i in result]
            print("r = ", r)
            result = result + r
            print("result: ", result)
        return result