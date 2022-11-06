class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = {}
        longest = 0
        l = 0
        r = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            while len(counter) == 3:
                longest += (len(s) - r)
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    counter.pop(s[l])
                l += 1
        return longest