# Problem: https://leetcode.com/problems/two-sum/

class Solution:
    
    # def dfs(self, root, k):
    #     if root:
    #         self.a.append(root.val)
    #         self.dfs(root.left, k)
    #         self.dfs(root.right, k)
    #     else:
    #         return
    
    d = dict()
    
    def dfs(self, i, number, target):
        difference = target - number
        if difference in self.d:
            return [i, self.d[difference][0]]
        else:
            self.d[number] = [i]
            return [-1, -1]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.d = dict()
        for i in range(len(nums)):
            res = self.dfs(i, nums[i], target)
            if res[0] != -1 and res[1] != -1:
                return res    
        return [-1, -1]
            
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].      