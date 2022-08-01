# Problem: https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d, island, m, n = dict(), 0, len(grid), len(grid[0])
        
        def dfs(i, j, m, n):
            if i < 0 or j < 0 or i == m or j == -1 or j == n or grid[i][j] != "1":
                return 
            else: 
                grid[i][j] = "#"
                dfs(i, j+1, m, n)
                dfs(i, j-1, m, n)
                dfs(i+1, j, m, n)
                dfs(i-1, j, m, n)
                
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1": 
                    island = island + 1
                    dfs(i, j, m, n)
                    
        return island