# Problem: https://leetcode.com/problems/course-schedule-ii/submissions/

class Solution:
    adjList = dict()
    color = dict()
    result = True
    
    top = list()
    
    def topologicalSort(self, n):
        if self.color[n] == "gray":
            self.result = False
            return
        
        elif self.color[n] == "green":
            return
        
        self.color[n] = "gray"
        
        for i in self.adjList[n]:
            self.topologicalSort(i)
            
        self.color[n] = "green"
        self.top.append(n)
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.adjList = dict()
        self.color = dict()
        self.result = True
        
        for i in range(numCourses):
            self.color[i] = "white"
            self.adjList[i] = set()
            
        for i in prerequisites:
            self.adjList[i[1]].add(i[0])
            
        # print(self.adjList)
                    
        if len(prerequisites) == 0:
            return range(numCourses)
        
        self.top = list()
        
        for i in range(numCourses):
            self.topologicalSort(i)

        if self.result == False:
            return []
        
        self.top.reverse()
        return self.top