# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode(0, next = head)
        prev = head
        current = head.next 
        
        while current:
            if current.val >= prev.val:
                prev = current
                current = current.next
                continue
            inSort = newNode 
            while current.val > inSort.next.val:
                inSort = inSort.next
            prev.next = current.next
            current.next = inSort.next
            inSort.next = current
            current = prev.next
        return newNode.next
            
                
            
        