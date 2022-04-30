# Problem: https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    b = False
    adj = dict()
    parents = set()
    
    def dfs(self, source, destination):
                
        # print("adj = ",adjNodes)        
        self.parents.add(source)
        # print("parents = ",parents)
        adjNodes = (self.adj[source] - self.parents)
        # print("adj = ",adjNodes)
        
        if destination in adjNodes:
            self.b = True
            return
                
        for eachNode in adjNodes:
            self.dfs(eachNode, destination)
                
        
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        self.b = False
        self.parents = set()
        
        # Adjacency 
        self.adj = dict()
        for lst in edges:
            if lst[0] not in self.adj.keys():
                self.adj[lst[0]] = set()
                
            self.adj[lst[0]].add(lst[1])
            
            if lst[1] not in self.adj.keys():
                self.adj[lst[1]] = set()
                
            self.adj[lst[1]].add(lst[0])

        self.dfs(source, destination)     
                    

                    
        return self.b

# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true