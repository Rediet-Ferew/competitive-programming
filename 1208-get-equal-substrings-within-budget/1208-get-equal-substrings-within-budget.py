class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        prefix = []
        for i in range(len(s)):
            dis = abs(ord(s[i]) - ord(t[i]))
            prefix.append(dis)
        l = 0
        r = 0
        total = 0
        max_len = 0
        while r < len(prefix):
            total += prefix[r] 
            while total > maxCost:
                total -= prefix[l]
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
                    
        