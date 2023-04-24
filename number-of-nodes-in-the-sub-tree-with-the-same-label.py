class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def findSubtree(parent, node, adj_list):
            
            count = [0] * 26
            idx = ord(labels[node]) - 97
            count[idx] += 1

            for item in adj_list[node]:
                if item != parent:
                    temp = findSubtree(node, item, adj_list)
                    for j in range(26):
                        count[j] += temp[j]
            t = ord(labels[node]) - 97
            ans[node] += count[t]
            return count


        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
       
        
        ans = [0] * n
        findSubtree(-1, 0, adj_list)
        
        return ans