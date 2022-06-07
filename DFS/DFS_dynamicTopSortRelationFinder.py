# Problem: https://leetcode.com/problems/course-schedule-iv/

class Solution:
    adjList = dict()
    ans = list()
    states = dict()
    
    def dfs(self, pre, cou):
        temp = False
        # If (pre, cou) is traversed before:
        if (pre, cou) in self.states:
            return self.states[(pre, cou)]
        
        if len(self.adjList[pre])==0:
            self.states[(pre, cou)] = False
            return False
        
        for i in self.adjList[pre]:
            if i == cou:
                self.states[(pre, i)] = True
                return True
            self.states[(i, cou)] = self.dfs(i, cou)
            temp = temp or self.states[(i, cou)]
        
        self.states[(pre, cou)] = temp
        return self.states[(pre, cou)]
    
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.adjList = dict()
        if len(prerequisites) == 0:
            return [False for i in range(len(queries))]
        else:
            self.ans = list()
        self.states = dict()
        
        # Making the graph        
        for i in range(numCourses):
            self.adjList[i] = set()
        for i in prerequisites:
            self.adjList[i[0]].add(i[1])
             
        # Getting the ans boolean array
        for i in queries:
            if (i[0], i[1]) in self.states:
                self.ans.append(self.states[(i[0], i[1])])
            else:
                self.states[(i[0], i[1])] = self.dfs(i[0], i[1])
                self.ans.append(self.states[(i[0], i[1])])
        
        return self.ans