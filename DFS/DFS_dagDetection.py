# Problem: https://leetcode.com/problems/course-schedule/

class Solution:
    adjList = dict()
    color = dict()
    result = True
    
    def dfs(self, n):
        if self.color[n] == "gray":
            self.result = False
            return 
        elif self.color[n] == "green":
            return
        
        self.color[n] = "gray"
        
        for i in self.adjList[n]:
            self.dfs(i)
            
        self.color[n] = "green"
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adjList = dict()
        self.color = dict()
        self.result = True
        
        for i in range(numCourses):
            self.color[i] = "white"
            self.adjList[i] = set()
            
        for i in prerequisites:
            self.adjList[i[0]].add(i[1])
                    
        if len(prerequisites) == 0:
            return True
        
        for i in range(numCourses):
            self.dfs(i)
        
        return self.result