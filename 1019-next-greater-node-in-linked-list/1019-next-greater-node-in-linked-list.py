# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        current = head
        answer = []
        stack = []
        i = -1
        while current:
            i += 1
            answer.append(0)
            while stack and stack[-1][1] < current.val:
                (currIndex, value) = stack.pop()
                answer[currIndex] = current.val
            stack.append((i, current.val))
            current = current.next
        return answer