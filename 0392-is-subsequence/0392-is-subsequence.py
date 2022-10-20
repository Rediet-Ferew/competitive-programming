class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        tp = 0
        sp = 0
        while tp < len(t) and sp < len(s):
            if t[tp] == s[sp]:
                tp += 1
                sp += 1
            else:
                tp += 1
        return sp == len(s)