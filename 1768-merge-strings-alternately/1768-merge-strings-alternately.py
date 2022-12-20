class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        pt1 = 0
        pt2 = 0
        ans = ''
        while pt1 < n1 and pt2 < n2:
            ans += word1[pt1]
            ans += word2[pt2]
            pt1 += 1
            pt2 += 1
        while pt1 < n1:
            ans += word1[pt1]
            pt1 += 1
        while pt2 < n2:
            ans += word2[pt2]
            pt2 += 1
        return ans