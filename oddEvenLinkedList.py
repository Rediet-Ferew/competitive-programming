# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        current = head
        temp = head.next
        odd = head
        even = head.next
        index = 1
        while current:
            if index > 2 and index%2 == 0:
                even.next = current
                even = even.next
            elif index > 2 and index%2 != 0:
                odd.next = current
                odd = odd.next
            index += 1
            current = current.next
        even.next = None
        odd.next = temp
        return head