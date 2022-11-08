class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # print(chr(65 + 32))
        # print("S".upper())
        # print("S".lower())
        def checker(s):
            if len(s) < 2:
                return ""
            # s = list(s)
            indices = set()
            for idx, ch in enumerate(s):
                indices.add(ch)
            for i in range(len(s)):
                if s[i].lower() in indices and s[i].upper() in indices:
                    continue
                s1 = checker(s[:i])
                s2 = checker(s[i+1:])
                if len(s1) >= len(s2):
                    return s1
                else:
                    return s2
            return s
        return (checker(s))
                                                                              
                    