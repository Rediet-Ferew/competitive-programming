# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        end = head
        length = 1
        while end.next:
            length += 1
            end = end.next
        # print(length)
        k = k % length
        if k == 0:
            return head
        current = head
        for i in range(length - k - 1):
            current = current.next
        newHead = current.next
        current.next = None
        end.next = head
        return newHead
        