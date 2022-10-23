# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0 
        current = head
        temp = []
        while current:
            count += 1
            temp.append(current.val)
            current = current.next
        if count <= 1:
            return 
        mid = count//2
        curr = head
        while mid > 1:
            curr = curr.next
            mid -= 1
        curr.next = curr.next.next
        return head
        
        
            