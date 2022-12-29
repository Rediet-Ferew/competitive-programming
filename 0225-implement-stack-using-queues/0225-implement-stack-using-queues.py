class MyStack:

    def __init__(self):
        self.stack = collections.deque()
        self.size = 0
        
    def push(self, x: int) -> None:
        
        self.stack.append(x)
        self.size += 1
        
    def pop(self) -> int:
        
        n = self.size
        i = 0
        num = 0
        
        while i < n - 1:
            temp = self.stack.popleft()
            self.stack.append(temp)
            i += 1
        num = self.stack.popleft()
        self.size -= 1
        return num
    
    
    def top(self) -> int:
        n = self.size
        i = 0
        num = 0
        while i < n:
            
            num = self.stack.popleft()
            self.stack.append(num)
            i += 1
            
        return num
    

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()