# Problem: https://leetcode.com/problems/loud-and-rich/

class Solution:
    adjList = dict()
    ans = dict()
    
    def dfs(self, n, quiet):
        if n in self.ans:
            return self.ans[n]
        
        mni = n
        for i in self.adjList[n]:
            r = self.dfs(i, quiet)
            if quiet[r] < quiet[mni]:
                mni = r

        self.ans[n] = mni
        return mni
        
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        self.adjList = dict()
        self.ans = dict()
        
        for i in range(len(quiet)):
            self.adjList[i] = set()
            
        for i in richer:
            self.adjList[i[1]].add(i[0])
            
        for i in range(len(quiet)):
            self.dfs(i, quiet)
            
        o = list()
        for i in range(len(quiet)):
            o.append(self.ans[i])
            
        return o