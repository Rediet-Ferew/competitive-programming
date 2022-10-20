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
        nodes = {}
        current = head
        size = 0
        while current:
            if current not in nodes:
                nodes[current] = size
            else:
                # print(nodes)
                return True
            current = current.next
            size += 1
        # print(nodes)
        return False
            
        