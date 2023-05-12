from typing import List
import collections
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, graph: List[List[int]]) -> bool:
		adj_list = collections.defaultdict(list)
		for i in range(len(graph)):
		    adj_list[i] = list(graph[i])
		q = collections.deque()
		visited = set()
		for i in range(V):
		    if i not in visited:
		        q.append([i, None])
		        visited.add(i)
		        while q:
		            node, p = q.popleft()
		            for neighbor in adj_list[node]:
		                if neighbor in visited and neighbor != p:
		                    return True
		                elif neighbor in visited and neighbor == p:
		                    continue
		                if neighbor not in visited:
		                    visited.add(neighbor)
		                    q.append((neighbor, node))
		                   
	    return False 
		      
		        
        
		        
		    

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
