# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        greater = ListNode()
        less_end = less
        greater_end = greater
        # current = head
        while head:
            if head.val < x:
                less_end.next = head
                less_end = less_end.next
            else:
                greater_end.next = head
                greater_end = greater_end.next
            head = head.next
        less_end.next = greater.next
        greater_end.next = None
        return less.next