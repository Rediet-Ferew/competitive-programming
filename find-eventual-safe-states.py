class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        no_cycle = set()
        ans = []
        def dfs(node):
            
            if node in no_cycle:
                
                return True

            if node in cycle:
                return False
            cycle.add(node)
           
            for neighbor in graph[node]:
               
                if not dfs(neighbor):
                    return False

           
            cycle.remove(node)
            no_cycle.add(node)
            ans.append(node)
            return True
        for i in range(len(graph)):
            cycle = set()
            dfs(i)
        return sorted(ans)