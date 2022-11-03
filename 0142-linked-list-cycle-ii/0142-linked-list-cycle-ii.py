# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashMap = {}
        size = 0
        current = head
        while current:
            if current not in hashMap:
                hashMap[current] = size
            else:
                return current
            current = current.next
        # return -1;
            