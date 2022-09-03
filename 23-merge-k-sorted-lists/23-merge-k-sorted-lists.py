# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final = []
        head = dummy = ListNode(0)
        for linked in lists:
            while linked:
                final.append(linked.val)
                linked = linked.next
        final.sort()
        for num in final:
            dummy.next = ListNode(num)
            dummy = dummy.next
        print(final)
        return head.next
            