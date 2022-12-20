class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_elements = {}
        for i, c in enumerate(s):
            s_elements[c] = 1 + s_elements.get(c, 0)
        for c in t:
            if c in s_elements:
                s_elements[c] -= 1
                if s_elements[c] == 0:
                    s_elements.pop(c)
            else:
                return c