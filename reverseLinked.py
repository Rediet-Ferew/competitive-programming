# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listToReverse = []
        if head == None:
            return None
        current = head
        listToReverse.append(current.val)
        while current.next != None:
            current = current.next
            listToReverse.append(current.val)
        listToReverse = listToReverse[::-1]
        print(listToReverse)
        head.val = listToReverse[0]
        current = head
        for i in range(1, len(listToReverse)):
            (current.next).val=  listToReverse[i]
            current = current.next
        return head
    