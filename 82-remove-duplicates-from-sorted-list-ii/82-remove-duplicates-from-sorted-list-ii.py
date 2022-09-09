
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = []
        current = head
        while current != None:
            newList.append(current.val)
            current = current.next
        count = Counter(newList)
        newList.clear()
        for key, value in count.items():
            if value == 1:
                newList.append(key)
        newNode = current = ListNode()
        
        for num in newList:
            current.next = ListNode(num)
            current = current.next
        return newNode.next
        
        
            
                