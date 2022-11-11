# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, next = head)
        l = dummy
        r = head
        while k > 1:
            r = r.next
            k -= 1
        beginning = r
        while r:
            l = l.next
            r = r.next
        beginning.val, l.val = l.val, beginning.val
        return head
        