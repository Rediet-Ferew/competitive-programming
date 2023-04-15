import collections
def dfs(adj, node, color, curr_col):

    color[node] = curr_col

    for u in adj[node]:

        if u in color:

            if color[u] == curr_col:
                return False 
            
        else:

            temp = dfs(adj, u, color, 1 - curr_col)

            if temp == False:
                return False
        
    return True


n = 1

while n:

    n = int(input())
    
    if n != 0:
        edge = int(input())
        
        adj = collections.defaultdict(list)
        color = {}

        for _ in range(edge):

            u, v = list(map(int, input().split()))
            adj[u].append(v)
            adj[v].append(u)

        ans = dfs(adj, 1, color, 1)
      
      
        if ans:
            print("BICOLOURABLE.")
        else:
            print("NOT BICOLOURABLE.")
        
