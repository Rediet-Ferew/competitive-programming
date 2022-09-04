# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0 
        current = head
        while current:
            count += 1
            current = current.next
        mid = count//2
        middle = head
        while mid > 0:
            middle = middle.next
            mid -= 1
        return middle
        