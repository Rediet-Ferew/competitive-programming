class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = list(p)
        p.sort()
        # print(p)
        indices = []
        n = len(p)
        m = len(s)
        left = 0
        right = n - 1
        while right < m:
            temp = list(s[left : right + 1])
            temp.sort()
            # print(temp)
            if temp == p:
                indices.append(left)
            left += 1
            right += 1
        return indices