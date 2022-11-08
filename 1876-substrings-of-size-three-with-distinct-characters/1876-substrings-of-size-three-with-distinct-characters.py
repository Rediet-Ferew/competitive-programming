class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = {}
        good_subs = 0
        if len(s) < 3:
            return 0
        for i in range(3):
            count[s[i]] = 1 + count.get(s[i], 0)
        if len(count) == 3:
            good_subs += 1
        l = 0
        r = 3
        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            count[s[l]] -= 1
            if count[s[l]] == 0:
                count.pop(s[l])
            if len(count) == 3:
                good_subs += 1
            l += 1
            r += 1
        return good_subs