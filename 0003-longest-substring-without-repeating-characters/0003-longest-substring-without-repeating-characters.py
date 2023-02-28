class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        visited = set()
        right = 0
        left = 0
        max_len = 0
        while right < n:
            ch = s[right]
            while ch in visited:
                visited.remove(s[left])
                left += 1
            visited.add(ch)
            max_len = max(max_len, right - left + 1)
            right += 1
            
            
        return max_len