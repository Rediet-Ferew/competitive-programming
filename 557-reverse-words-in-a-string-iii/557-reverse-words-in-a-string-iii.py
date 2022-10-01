class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split()
        for i in range(len(slist)):
            slist[i] = slist[i][::-1]
        return " ".join(slist)