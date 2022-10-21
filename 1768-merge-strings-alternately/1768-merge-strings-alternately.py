class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        first = 0
        second = 0
        while first < len(word1) and second < len(word2):
            result += word1[first]
            result += word2[second]
            first += 1
            second += 1
        while first < len(word1):
            result += word1[first]
            first += 1
        while second < len(word2):
            result += word2[second]
            second += 1
        return result
#         list1 = list(word1)
#         list2 = list(word2)
#         first = 0
#         second = 0
#         while list1 and list2:
#             result += list1[0]
#             result += list2[0]
#             del list1[0]
#             del list2[0]
            
#         i = 0
#         while list1 and i < len(list1):
#             result += list1[i]
#             i += 1
#         j = 0
        
#         while list2 and j < len(list2):
#             result += list2[j]
#             j += 1
#         return result
            