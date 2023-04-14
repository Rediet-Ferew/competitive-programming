class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def dfs(dislike, node, color, curr_col):
            color[node] = curr_col
            for u in dislike[node]:
                if u in color:
                    if color[u] == curr_col:
                        return False 
                else:
                    temp = dfs(dislike, u, color, 1 - curr_col)
                    if temp == False:
                        return False
                
            return True
        dislike = defaultdict(list)
        
        for u, v in dislikes:
            
            dislike[u].append(v)
            dislike[v].append(u)
        
        # print(bool(-1))
        color = {}
        print(color)
        for i in range(1, n + 1):
            if i not in color:
                
                if not dfs(dislike, i, color, 1):
                    return False
         
            # print(color)
            
        return True