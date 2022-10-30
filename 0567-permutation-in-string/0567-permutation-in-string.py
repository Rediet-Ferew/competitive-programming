class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = sorted(s1)
        s1 = "".join(s1)
        left = 0
        right = n - 1
        while right < len(s2):
            sub = sorted(s2[left:right + 1])
            sub = "".join(sub)
            if sub == s1:
                return True
            left += 1
            right += 1
        return False