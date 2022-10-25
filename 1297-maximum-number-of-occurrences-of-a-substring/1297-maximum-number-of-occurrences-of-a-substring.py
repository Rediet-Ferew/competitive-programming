class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        r = 0
        
        count = {}
        max_occ = 0
        while r < len(s) - minSize + 1:
            sub = s[r: r+minSize]
            
            if len(set(sub)) <= maxLetters:
                count[sub] = 1 + count.get(sub, 0)
                max_occ = max(count[sub], max_occ)
            r += 1
        
        return max_occ