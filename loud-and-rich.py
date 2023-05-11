class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj_list = {}
        for greater, less in richer:
            if less in adj_list:
                adj_list[less].append(greater)
            else:
                adj_list[less] = [greater]
            
        print(adj_list)
    
        ans = [len(quiet)] * (len(quiet))
        @lru_cache(None)
        def dfs(node):
           
            min_val = [quiet[node], node]
            if node in adj_list:
                for neighbor in adj_list[node]:
                    temp = dfs(neighbor)
                    if temp[0] <= min_val[0]:
                        min_val = temp
                    
            return min_val
         
        
        for i in range(len(quiet)):
            
            temp = dfs(i)
            ans[i] = temp[1]
        
        # print(ans)
        return ans