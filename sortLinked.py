# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        current = head
        sortedList = []
        sortedList.append(current.val)
        while current.next != None:
            current = current.next
            sortedList.append(current.val)
        sortedList = sorted(sortedList)
        print(sortedList)
        tail = head
        head.val = sortedList[0]
        for num in sortedList:
            tail.val = num
            tail = tail.next
        return head
