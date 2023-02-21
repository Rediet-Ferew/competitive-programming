# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(head):
            curr = head
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            return prev
        
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next
    
        rev = reverse(slow)
        
        first = head
        second = rev
        max_sum = float('-inf')
        while first and second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        return max_sum
        
#         idx = {}
        
#         cnt = 0
#         curr = head
#         while curr:
#             curr = curr.next
#             cnt += 1
            
#         max_sum = float('-inf')
#         curr_2 = head
#         pos = 0
#         while curr_2:
            
#             if (cnt - pos - 1) in idx:
#                 max_sum = max(max_sum , idx[cnt - pos - 1] + curr_2.val)
#             else:
#                 idx[pos] = curr_2.val
                
#             pos += 1
#             curr_2 = curr_2.next
        
#         return max_sum