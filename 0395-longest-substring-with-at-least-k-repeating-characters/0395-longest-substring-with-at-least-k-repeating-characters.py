class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        count = Counter(s)
        if len(s) == 0:
            return 0
        if min(count.values()) >= k:
            return len(s)
        
        length = 0
        for i in range(len(s)):
            if count[s[i]] < k:
                length = max(self.longestSubstring(s[:i], k),self.longestSubstring(s[i+1:], k))
                break
            length += 1
        return length