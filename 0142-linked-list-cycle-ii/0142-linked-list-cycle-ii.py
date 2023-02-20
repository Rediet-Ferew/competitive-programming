# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        cycle = False
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break
        if not cycle:
            return 
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow  
        
        
        
        # hashMap = set()
        # size = 0
        # current = head
        # while current:
        #     if current not in hashMap:
        #         hashMap.add(current)
        #     else:
        #         return current
        #     current = current.next
        # return -1;
            