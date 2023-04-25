class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in roads:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        temp = []
        for i in graph.keys():
            temp.append(i)
            
        mx = 0
        
        for i in range(len(graph.keys())):
            for j in range(i + 1, len(temp)):
          
                if temp[i] in graph[temp[j]]:
            
                    mx = max(mx, len(graph[temp[i]] + graph[temp[j]]) - 1)
               
                    
                else:   
              
                    mx = max(mx, len(graph[temp[i]] + graph[temp[j]]))
                
        return mx