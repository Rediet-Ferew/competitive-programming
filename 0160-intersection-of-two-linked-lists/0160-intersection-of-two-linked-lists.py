
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        Aptr = headA
        nums = {}
        size = 0
        while Aptr:
            nums[Aptr] = size
            Aptr = Aptr.next
            size += 1
        B = headB
        while B:
            if B in nums:
                return B
            B = B.next
        return 
            