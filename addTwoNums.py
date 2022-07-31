# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = ""
        nums2 = ""
        current1 = l1
        current2 = l2
        nums1 += str(current1.val)
        nums2 += str(current2.val)
        while current1.next != None and current2.next != None:
            current1 = current1.next
            current2 = current2.next
            nums1 += str(current1.val)
            nums2 += str(current2.val)
        while current1.next == None and current2.next != None:
            current2 = current2.next
            nums2 += str(current2.val)
        while current1.next != None and current2.next == None:
            current1 = current1.next
            nums1 += str(current1.val)
        added = int(nums1[::-1]) + int(nums2[::-1])
        addedstr = str(added)
        addedstr = addedstr[::-1]
        l1.val = addedstr[0]
        current = l1
        for i in range(1, len(addedstr)):
            (current.next).val = addedstr[i]
            current = current.next
        return l1
            