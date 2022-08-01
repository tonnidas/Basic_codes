# Problem: https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hist = list()
        track = dict()
        
        for i in range(len(s)):
            if s[i] not in track:
                track[s[i]] = len(hist)
                hist.append((i, -1))
            else:
                temp = hist[track[s[i]]]
                hist[track[s[i]]] = (temp[0], i)
        
        for i in range(1, len(hist), 1):
            if hist[i-1][1] > hist[i][0]: # Collapse
                hist[i] = (min(hist[i-1][0], hist[i][0]), max(hist[i-1][1], hist[i][1]))
                hist[i-1] = None
                
        res = list()
        for i in range(0, len(hist), 1):
            if hist[i] == None: continue
            if hist[i][1] != -1: res.append(hist[i][1] - hist[i][0] + 1)
            if hist[i][1] == -1: res.append(1)
        
        return res