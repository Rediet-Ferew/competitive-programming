class ListNode:
    def __init__(self, val =0, next = None, prev = None):
        self.val = val 
        self.next = next
        self.prev = prev
class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.head = ListNode()
        self.size = 0

    def insertFront(self, value: int) -> bool:
        node = ListNode(value)
        if self.size < self.capacity:
            nxt = self.head.next
            self.head.next = node
            node.next = nxt
            if nxt:
                nxt.prev = node
            node.prev = self.head
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        node = ListNode(value)
        curr = self.head
        while curr.next:
            curr = curr.next
        if self.size < self.capacity:
            nxt = curr
            curr.next = node
            node.prev = nxt
            self.size += 1
            return True
        else:
            return False
    def deleteFront(self) -> bool:
        if self.size > 0:
            curr = self.head.next
            nxt = curr.next
            self.head.next = nxt
            if nxt:
                nxt.prev = self.head
            self.size -= 1
            return True
        else:
            return False
    def deleteLast(self) -> bool:
        if self.size > 0:
            curr = self.head
            while curr.next:
                curr = curr.next

            nxt = curr.next
            prv = curr.prev
            prv.next = None
            curr.prev = None
            self.size -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        else:
            curr = self.head.next
            return curr.val

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            return curr.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


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