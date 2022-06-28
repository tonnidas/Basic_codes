# Problem: https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1:
            return intervals
        
        intervals = sorted(intervals, key=itemgetter(0))
        for i in range(len(intervals)-1):
            m = intervals[i]
            n = intervals[i+1]
            if m[0] == n[0] or m[1] == n[1] or m[1] >= n[0]:
                intervals[i] = None
                intervals[i+1] = [min(m[0], n[0]), max(m[1], n[1])]

        res = list()
        for i in range(len(intervals)):
            if intervals[i] != None:
                res.append(intervals[i])
        return res