# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        else:
            
            current = head
            while current != None:
                if current.next == None:
                    break
                (current.val, current.next.val) = (current.next.val, current.val)
                current = current.next.next
            return head