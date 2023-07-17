# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, next = head)
        prev = head
        curr = head.next 
        
        while curr:
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
                continue
            inSort = dummy 
            while curr.val > inSort.next.val:
                inSort = inSort.next
            prev.next = curr.next
            curr.next = inSort.next
            inSort.next = curr
            curr = prev.next
        return dummy.next