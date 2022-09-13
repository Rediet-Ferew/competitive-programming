class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        changed.sort()
        if len(changed) % 2 != 0:
            return []
        # print(changed)
        count = Counter(changed)
        
        for num in changed:
            if num == 0 and count[0] >= 2:
                count[num] -= 2
                original.append(num)
            elif num != 0 and count[num] and count[num * 2]:
                count[num] -= 1
                count[num * 2] -= 1
                original.append(num)
            
        # print(original)
        if len(original) == len(changed) //2:
            return original
        else:
            return  []
#         while changed and len(changed) > 1:
#             small = changed[0]
#             num = 2 * small
#             if num not in changed[1:] or len(changed) == 1:
#                 original.clear()
#                 return 
#             if num in changed:
#                 changed.remove(num)
#                 original.append(small)
#                 del changed[0]
                
#         return original
        
        
            
        