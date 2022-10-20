# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        3 -> 2 -> 0 -> 4->
        [3->, 2->, 0->,4 -> ]
        """
        nodes = []
        current = head
        while current:
            if current not in nodes:
                nodes.append(current)
            else:
                # print(nodes)
                return True
            current = current.next
        # print(nodes)
        return False
            
        