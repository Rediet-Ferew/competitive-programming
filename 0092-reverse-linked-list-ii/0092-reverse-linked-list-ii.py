# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, next = head)
        
        curr = dummy
        count = 1
        while count < left:
            curr = curr.next
            count += 1
        l = curr.next
        r = l.next
        
        for idx in range(right - left):
            
            l.next = r.next
            r.next = curr.next
            curr.next = r
            r = l.next
        return dummy.next