# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        dummy = ListNode(0, next=head)
        left = dummy
        while right and n > 0:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
        # counter = 1
        # current = head
        # while current.next != None:
        #     counter += 1
        #     current = current.next
        # counter = counter - n
        # current2 = head
        # if counter == 0:
        #     return head.next
        # while counter > 1:
        #     current2 = current2.next
        #     counter -= 1
        # current2.next = (current2.next).next
        # return head