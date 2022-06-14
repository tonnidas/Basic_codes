# Prob: https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def dfs(node):
            if hist[node] == True:
                return
            else:
                hist[node] = True
                for each in directParent[node]:
                    res[node].add(each)
                    dfs(each)
                    res[node] = res[node].union(res[each])
            
        res = list()
        hist = dict()
        directParent = list()
        fin = list()
        
        for i in range(n):
            res.append(set())
            hist[i] = False
            directParent.append(set())
        
        for edge in edges:
            directParent[edge[1]].add(edge[0])
                    
        for i in range(n):
            dfs(i)            
        
        for i in range(n):
            fin.append(list(sorted(res[i])))
        
        return fin
            
            