class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def get(self, index: int) -> int:
        
        if self.head == None:
            return None
        current = self.head
        counter = index
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head ==self.tail == None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
        self.size += 1
    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head ==self.tail == None:
            self.head = self.tail = newNode
        else:
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
            
        self.size += 1
    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            for i in range(index -1):
                current = current.next
            newNode.next = current.next
            current.next = newNode
        self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.size == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
        elif index == self.size -1:
            self.tail = prev
        else:
            prev = None
            current = self.head
            for i in range(index):
                prev = current
                current = current.next
            prev.next = current.next
                
        
        self.size -= 1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)