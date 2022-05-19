# Problem: https://leetcode.com/problems/3sum/

class Solution:
    finallist = set()
    d = dict()
    
    def mtd(self, i, j, numsi, numsj, target):
        difference = target - (numsi + numsj)
        
        if difference in self.d:
            lst = [difference, numsi, numsj]
            self.finallist.add(tuple(lst))
            
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.d = dict()
        self.finallist = set()
        target = 0
        
        nums.sort()
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums),1):
                self.mtd(i, j, nums[i], nums[j], target)
                
            if nums[i] not in self.d:
                self.d[nums[i]] = set()
            self.d[nums[i]].add(i)
                   
        return self.finallist

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]