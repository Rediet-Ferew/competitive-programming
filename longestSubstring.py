class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        listStr = []
        lengths = []
        for c in s:
            if c not in listStr:
                listStr.append(c)
            else:
                listStr.append(listStr.pop())
                lengths.append(len(listStr))
                listStr.clear()
                
        lengths.append(len(listStr))
        
        return max(lengths)