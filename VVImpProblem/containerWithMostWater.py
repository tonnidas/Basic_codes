# Problem: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        def calcWater(i, j):
            num = min(height[i], height[j]) * abs(j - i)
            nonlocal water
            water = max(water, num)
            
        st = True
        i, j = 0, len(height)-1
        while(st):
            print("i, j = ", i, j)
            calcWater(i, j)
            if height[i] < height[j]:
                i = i + 1
            elif height[i] > height[j]:
                j = j - 1
            else:
                j = j - 1    
                
            if j == -1 or i == len(height):
                st = False
            
        return water