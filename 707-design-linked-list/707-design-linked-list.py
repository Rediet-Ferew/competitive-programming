class MyLinkedList:

    def __init__(self):
        self.linked_list = []
        self.size = 0
    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        return self.linked_list[index]

    def addAtHead(self, val: int) -> None:
        self.linked_list.insert(0, val)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.linked_list.append(val)
        self.size += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.linked_list.append(val)
            self.size += 1
        elif index > self.size:
            return 
        else:
            self.linked_list.insert(index, val)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        else:
            del self.linked_list[index]
            self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)