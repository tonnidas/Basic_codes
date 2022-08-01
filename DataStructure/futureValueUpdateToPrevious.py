# Problem: https://leetcode.com/problems/daily-temperatures/


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        sete = list()
        
        for i, temp in enumerate(temperatures):
            while len(sete) != 0 and temperatures[sete[-1]] < temp:
                # print("sete = ", sete)
                prev = sete.pop()
                # print(prev, sete)
                result[prev] = i - prev
            # print("-----------")
            sete.append(i)
        return result