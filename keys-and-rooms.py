class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        not_opened = set()
        for i in range(1, len(rooms)):
            not_opened.add(i)
        
        q = collections.deque()
        for r in rooms[0]:
            q.append(r)
            not_opened.remove(r)
            
        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                val = q.popleft()
                
                for r in rooms[val]:
                    if r in not_opened:
                        not_opened.remove(r)
                        q.append(r)
        if not_opened:
            return False
        else:
            return True