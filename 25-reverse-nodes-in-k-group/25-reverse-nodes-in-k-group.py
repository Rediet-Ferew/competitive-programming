# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        def getKth(current, k):
            while current and k > 0:
                current = current.next
                k -= 1
            return current
        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev, current = kth.next, groupPrev.next
            while current != groupNext:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            temp2 = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp2
        return dummy.next
        