class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        pt1 = 0
        pt2 = 0
        merged = ""
        
        while pt1 < n1 and pt2 < n2:
                 
            if word1[pt1:] > word2[pt2:]:
                merged += word1[pt1]
                pt1 += 1

            else:
                merged += word2[pt2]
                pt2 += 1
        
        merged += word1[pt1:]
        merged += word2[pt2:]
            
        return merged
    