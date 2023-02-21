# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = 0
        curr = head
        prev = ListNode()
        while curr:
            prev = curr
            curr = curr.next
            n += 1
        last = prev
    
        
        k = k % n
        if k == 0:
            return head
        new_head = ListNode()
        current = head
        for i in range(n - k - 1):
            current = current.next
        
        new_head.next = current.next
        
        current.next = None
        last.next = head
        return new_head.next