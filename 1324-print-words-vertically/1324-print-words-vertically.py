class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = len(words)
        #finding the maximum length among the words
        sorted_words = sorted(words, key = len)
        max_len = len(sorted_words[-1])
        
        #list to hold the vertical traverse of words
        vertical_traverse = [[" " for k in range(n)] for _ in range(max_len)]
        
        #position each letter
        for i in range(n):
            m = len(words[i])
            
            for j in range(m):
                vertical_traverse[j][i] = words[i][j]
        
        ans = []
        #remove trailing spaces from the right
        for verticals in vertical_traverse:
            
            col = "".join(verticals).rstrip()
            ans.append(col)
        
        return ans
        