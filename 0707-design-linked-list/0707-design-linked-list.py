class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, idx: int) -> int:
        if idx < 0 or idx >= self.size or not self.head:
            return -1
        # if idx == 0:
        #     return self.head.val
        
        current = self.head
        num = -1
        indx = 0
        while current:
            if indx == idx:
                num = current.val
                break
            current = current.next
            indx += 1
        return num

        # return current.val


    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head)
        
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val, None)

        if not self.head:
            self.head = node

        else:

            current = self.head
            while current.next:
                current = current.next

            current.next = node
        self.size += 1

    def addAtIndex(self, idx: int, val: int) -> None:
        node = Node(val)
        if idx > self.size or idx < 0:
            return
        if idx == 0:
            self.addAtHead(node.val)
            self.size += 1
            return
        if idx == self.size:
            self.addAtTail(node.val)
            return
        
        else:
            
            current = self.head
            indx = 0
            while current:
                if indx == idx - 1:
                    temp = current.next
                    current.next = node
                    node.next = temp
                    break
                current = current.next
                indx += 1

            
            
            self.size += 1
    
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0 or not self.head:
            return
        
        #the pointer needs to stop at the previous node of the node we are deleting
        #but if index is 0 there is not previous element so handle that case
        else:
            if index == 0:
                self.head = self.head.next

            idx = 0
            current = self.head
            while current:
                if idx == index - 1:
                    current.next = current.next.next
                    break
                current = current.next
                idx += 1

            self.size -= 1
                
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)