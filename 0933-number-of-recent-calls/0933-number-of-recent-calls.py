class RecentCounter:

    def __init__(self):
        self.requests = 0
        self.q = collections.deque()
    def ping(self, t: int) -> int:
        start = t - 3000
        
        while self.q and start > self.q[0]:
            self.q.popleft()
            self.requests -= 1
            
        self.q.append(t)
        
        self.requests += 1
        
        return self.requests

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)