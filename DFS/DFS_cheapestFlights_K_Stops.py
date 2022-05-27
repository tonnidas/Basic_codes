# Problem: https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = dict()
        dcost = dict()
        dmn = dict()
        
        for i in range(len(flights)):
            if flights[i][0] not in d:
                d[flights[i][0]] = list()
            d[flights[i][0]].append(flights[i])
            
        for i in range(n):
            dmn[i] = 0
            dcost[i] = list()
            for j in range(101):
                dcost[i].append(100000000)

        finalcost = list()
        
        def dfs(sc, kcount, cost):
            if kcount > k:
                return
            
            curMinLen = dmn[sc]
            curMinCost = dcost[sc][curMinLen]
            
            if (kcount < curMinLen or cost < curMinCost) and dcost[sc][kcount] > cost:
                if cost < curMinCost:
                    dmn[sc] = kcount
                
                dcost[sc][kcount] = cost
            
                if sc in d and len(d[sc]) != 0:
                    for i in range(len(d[sc])):
                        if d[sc][i][1] == dst:
                            finalcost.append(cost + d[sc][i][2])
                        else:
                            dfs(d[sc][i][1], kcount + 1, cost + d[sc][i][2])
            return
        
        dfs(src,0,0)
        
        if len(finalcost) == 0:
            return -1
        else:
            return min(finalcost)