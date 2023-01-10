class DataStream:

    def __init__(self, value: int, k: int):
        
        self.stream = collections.deque()
        self.value = value
        self.k = k
        self.count = 0
        
    def consec(self, num: int) -> bool:
        
        if num == self.value:
            self.count += 1
        
        if len(self.stream) == self.k:
            
            removed = self.stream.popleft()
            
            if removed == self.value:
                self.count -= 1
        self.stream.append(num)
        if self.count == self.k:
            return True
        return False
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)