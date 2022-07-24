class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None] * k
        self.limit = k
        self.size = 0
        self.front = 0
        self.rear = self.size - 1 

    def insertFront(self, value: int) -> bool:
        if self.size == self.limit:
            return False
        elif self.isEmpty():
            self.deque[self.front] = self.deque[self.rear] = value
            self.size += 1
        else:
            self.deque[self.front] = value
            # self.front = (self.front + 1) % self.limit
            self.size += 1
        return True
    def insertLast(self, value: int) -> bool:
        if self.size == self.limit:
            return False
        elif self.isEmpty():
            self.deque[self.front] = self.deque[self.rear] = value
            self.size += 1
        else:
            self.deque[self.rear] = value
            # self.rear = (self.rear - 1) % self.limit
            self.size += 1
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque.remove(self.deque[self.front])
            self.size -= 1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque.pop()
            self.size -= 1
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.rear]

    def isEmpty(self) -> bool:
        
        if self.size == 0:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if self.size == self.limit:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()