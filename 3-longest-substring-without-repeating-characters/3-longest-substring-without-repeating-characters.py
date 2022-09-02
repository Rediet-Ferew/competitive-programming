class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_length = 0
        if len(s) == 1:
            return 1
        for i in range(1, len(s)):
            while s[i] in s[start: i]:
                start += 1
            max_length = max(max_length, i - start + 1)
        return max_length