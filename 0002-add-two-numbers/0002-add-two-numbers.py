# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = l1
        curr_2 = l2
        pre = 0
        dummy = ListNode()
        d = dummy
        while curr_1 or curr_2:
            #get numbers
            num_1 = curr_1.val if curr_1 else 0
            num_2 = curr_2.val if curr_2 else 0
            sum_ = num_1 + num_2 + pre
            mod = sum_ % 10
            pre = sum_ // 10
            d.next = ListNode(mod)
            d = d.next 
            
            if curr_1: curr_1 = curr_1.next
            if curr_2: curr_2 = curr_2.next
        if pre:
            d.next = ListNode(pre)
            d = d.next 
            
        return dummy.next
            