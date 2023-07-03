# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = ListNode(0)
        # dummy = ListNode(0)
        for linked in lists:
            while linked:
                heapq.heappush(heap, linked.val)
                linked = linked.next
        if heap:
            val = heapq.heappop(heap)
            head.val = val
        else:
            return None
        dummy = head
        while heap:
            v = heapq.heappop(heap)
            node = ListNode(v)
            head.next = node
            head = node
        return dummy