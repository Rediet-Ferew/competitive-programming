class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        adj_list = {}
        
        for u, v in adjacentPairs:
            if u not in adj_list:
                adj_list[u] = [v]
            else:
                adj_list[u].append(v)
            
            if v not in adj_list:
                adj_list[v] = [u]
            else:
                adj_list[v].append(u)

        # print(adj_list)
        order = [0] * len(adj_list)
        q = collections.deque()
        visited = set()
        for key, val in adj_list.items():
            if len(val) == 1:
                
                if not order[0]:
                    order[0] = key
                    q.append((key, None, 0))
                    
                elif not order[-1]:
                    order[-1] = key
                    q.append((key, None, len(adj_list) - 1))
                visited.add(key)
        def isInBound(idx):
            if 0 <= idx <= len(adj_list) - 1:
                return True
            return False
        
        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                node, parent, idx = q.popleft()
                for neighbor in adj_list[node]:
                    if neighbor in visited:
                        continue
                    else:
                        pos1 = idx + 1
                        pos2 = idx - 1
                        if isInBound(pos1) and not order[pos1]:
                            order[pos1] = neighbor
                            q.append((neighbor, val, pos1))
                            visited.add(neighbor)
                        elif isInBound(pos2) and not order[pos2]:
                            order[pos2] = neighbor
                            q.append((neighbor, val, pos2))
                            visited.add(neighbor)
        return order