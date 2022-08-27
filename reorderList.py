# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        prev = None
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        first, last = head, prev
        while last:
            temp1 = first.next
            temp2 = last.next
            first.next = last
            last.next = temp1
            first = temp1
            last = temp2
            
            
            
        
        
            
            
        
            
            