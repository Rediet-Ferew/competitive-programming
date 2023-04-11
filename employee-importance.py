"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        #build an adjacency list

        linkage = defaultdict(list)

        emp_importance = defaultdict(int)

        for i in range(len(employees)):
            node = employees[i].id
            imp = employees[i].importance
            sub = employees[i].subordinates
            linkage[node].extend(sub)
            emp_importance[node] =  imp

        visited = set()
        
        def dfs(node, visited):
            
            nonlocal total_importance
            
            if node in visited:
                return 
            visited.add(node)
            total_importance += emp_importance[node]
            for j in range(len(linkage[node])):
                if linkage[node][j] not in visited:
                    
                    dfs(linkage[node][j], visited)
        total_importance = 0
        dfs(id, visited)
        return total_importance