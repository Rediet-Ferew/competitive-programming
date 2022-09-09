# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palin = []
        current = head
        palin.append(current.val)
        while current.next != None:
            current = current.next
            palin.append(current.val)
            
        if palin == palin[::-1]:
            return True
        else:
            return False