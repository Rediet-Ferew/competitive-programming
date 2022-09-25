class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.limit = k
        # self.rear = 0
        # self.front = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.limit:
            return False
        self.queue.append(value)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        self.queue.pop(0)
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        # front = 0
        # while self.queue[front] == None:
        #     front += 1
        return self.queue[0]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        # last = self.rear
        # while self.queue[last] == None:
        #     last -= 1
        return self.queue[-1]

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


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()