# Problem: https://leetcode.com/problems/kth-largest-element-in-an-array/


# Python3 program to demonstrate working of heapq
from heapq import heappop, heappush, heapify
 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Making all elements of the array nagetive, so that heapify method can put the lowest number on top
        # and when we pop a number, it will be that lowest number, but if we multiply it with a -1, we will get original
        # positive number. This way, pop as many times as need.
        # We could pop kth lowest number in similar fashion
        
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]
        
        heapify(nums)
            
        for i in range(k-1):
            r = heappop(nums)
            # print(r)

        return -1 * heappop(nums)