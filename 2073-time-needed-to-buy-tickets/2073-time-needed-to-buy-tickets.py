class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        q = collections.deque()
        
        for idx, t in enumerate(tickets):
            q.append((t, idx))
            
        
        time = 0
        
        while q:
            
            time += 1
            ticket, idx = q.popleft()
            ticket -= 1
            
            if ticket > 0:
                q.append((ticket, idx))
                
            elif ticket == 0 and idx == k:
                return time
        
        # return ans[k]