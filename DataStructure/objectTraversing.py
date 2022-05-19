# Problem: https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""    
class Solution:
    d = dict()
    
    def dfs(self, number):
        employee = self.d[number]
        sum = employee.importance

        for j in range(len(employee.subordinates)):
            sum = sum + self.dfs(employee.subordinates[j])     
        return sum
                      
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        for i in range(len(employees)):
            self.d[employees[i].id] = employees[i]
        return self.dfs(id)