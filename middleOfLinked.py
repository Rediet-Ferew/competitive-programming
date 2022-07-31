# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        current = head
        store.append(current.val)
        while current.next != None:
            current = current.next
            store.append(current.val)
        if len(store) == 1:
            return head
        middle = store[len(store)//2]
        counter = 1
        current = head 
        while (current.next) != None:
            current = current.next
            counter += 1
            if (counter < len(store) // 2) or current.val != middle:
                break
        current = current.next
        head = current
        current2 = head
        while current2.next != None:
            current2 = current2.next
        return head
        