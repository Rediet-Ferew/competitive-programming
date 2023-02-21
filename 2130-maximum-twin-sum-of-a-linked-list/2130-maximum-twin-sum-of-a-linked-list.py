# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        idx = {}
        
        cnt = 0
        curr = head
        while curr:
            curr = curr.next
            cnt += 1
            
        max_sum = float('-inf')
        curr_2 = head
        pos = 0
        while curr_2:
            
            if (cnt - pos - 1) in idx:
                max_sum = max(max_sum , idx[cnt - pos - 1] + curr_2.val)
            else:
                idx[pos] = curr_2.val
                
            pos += 1
            curr_2 = curr_2.next
        
        return max_sum