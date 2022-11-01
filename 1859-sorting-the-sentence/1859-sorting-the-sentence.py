class Solution:
    def sortSentence(self, s: str) -> str:
        final = [""] * 10
        temp = ""
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if not s[i].isnumeric():
                temp += s[i]
            else:
                idx = int(s[i])
                final[idx] = temp
                temp = ""
        res = ""
        for j in range(10):
            if final[j] != "":
                res +=( final[j] + " ")
        return res[:-1]
            
        