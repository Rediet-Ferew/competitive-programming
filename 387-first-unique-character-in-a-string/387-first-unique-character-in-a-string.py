class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        count = Counter(s)
        # print(count)
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1