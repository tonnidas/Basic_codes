# Problem: https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        checking = set()
        auxilary = [None] * len(matrix)
        
        for i in range(len(matrix)):
            auxilary[i] = [None] * len(matrix[i])
            
            for j in range(len(matrix[i])):
                if matrix[i][j] == "1": matrix[i][j] = 1
                else: matrix[i][j], auxilary[i][j] = 0, 0
                    
                if j == 0 or i == 0: auxilary[i][j] = matrix[i][j]
                checking.add(matrix[i][j])
              
        maxim = -1
        # If there are all zeros or all ones in a matrix, maxim = zero or one depending on what is all element 
        # If there are ones and zeros in a matrix, maxim = 1 as atleast one square of length can be found
        if len(checking) == 1: 
            maxim = checking.pop()
            print(maxim)
        else: maxim = 1

        for i in range(1, len(auxilary)):
            for j in range(1, len(auxilary[i])):
                m = min(auxilary[i][j-1], auxilary[i-1][j])
                m = min(m, auxilary[i-1][j-1])
                if auxilary[i][j] == None: auxilary[i][j] = m + 1
                maxim = max(maxim, auxilary[i][j])
                        
        return maxim * maxim