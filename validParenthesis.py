class Solution:
    def isValid(self, s: str) -> bool:
        parent = {'{':'}', '[' : ']', '(': ')'}
        list1 = []
        list2 = []
        for i in s:
            list1.append(i)
        list1 = list1[::-1]
        n = len(list1)
        l = 0
        for i in range(n):
            if list[n - 1] in parent.values():
                break
            elif list1[n - 1] in parent.keys():
                list2.append(list1.pop())
                l +=1
            elif list1[n - 1] in parent.values():
                if len(list2) and (parent.get(list2[l - 1]) == list1[n -1]):
                    list2.pop()
                    list1.pop()
                else:
                    break
            n = len(list1)
            l = len(list2)
            
        
        if len(list1) == 0 and len(list2) == 0:
            return True
        else:
            return False
        