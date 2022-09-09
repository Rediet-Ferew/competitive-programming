# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current = head
        newList = [current.val]
        newSum = []
        while current.next:
            current = current.next
            newList.append(current.val)
        for i in range(len(newList)//2):
            newSum.append(newList[i] + newList.pop())
        return max(newSum)