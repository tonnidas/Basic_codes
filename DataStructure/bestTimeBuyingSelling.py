# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_prof = 0

        for pr in prices:

            max_prof = max(max_prof, pr - lowest)
            lowest = min(pr,lowest)
        return max_prof