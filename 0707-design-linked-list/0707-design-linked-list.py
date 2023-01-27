class Node:
    
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class MyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get(self, idx: int) -> int:
        if idx < 0 or idx >= self.size or not self.head:
            return -1
        
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

        


    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head = self.tail = Node(val, next=None, prev=None)
            
        else: 
            head_node = self.head
            node = Node(val, next = head_node, prev = None)
            head_node.prev = node
            self.head = node
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)

        if self.size == 0:
            self.head = self.tail = node

        else:
            tail_node = self.tail
            tail_node.next = node
            node.prev = tail_node
            self.tail = node
#             current = self.head
#             while current.next:
#                 current = current.next

#             current.next = node
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
                    # if current.next:
                    temp = current.next
                    current.next = node
                    node.prev = current
                    node.next = temp
                    temp.prev = node
                    # current.next = node
                    # node.next = temp
                    break
                current = current.next
                indx += 1

            
            
            self.size += 1
#             current = self.head
#             indx = 0
#             while current:
#                 if indx == idx - 1:
#                     temp = current.next
#                     current.next = node
#                     node.next = temp
#                     break
#                 current = current.next
#                 indx += 1

            
            
#             self.size += 1
    def print_list(self):
        linked = []
        current = self.head
        while current:
            linked.append([current.val, current.next, current.prev])
            current=current.next
        print(linked)
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
            # previous = Node()
            while current:
                if idx == index:
                    del_node = current
                    prev_node = del_node.prev
                    nxt_node = del_node.next
                    if prev_node:
                        prev_node.next = nxt_node
                    else:
                        self.head = nxt_node
                    if nxt_node:
                        nxt_node.prev = prev_node
                    else:
                        self.tail = prev_node
                        
                    break
                else:
                    current = current.next
                    
                
                idx += 1

            self.size -= 1
        # self.print_list()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)