class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = 0
        curr = ""
        res = []
        while i < n:
            if s[i] != " ":
                j = i
                while  j < n and s[j] != " ":
                    curr += s[j]
                    j += 1
                res.append(curr)
                curr = ""
                i = j
            else:
                i += 1
        res = res[::-1]
        return " ".join(res)
        # n = len(s)
        # stack = []
        # i = 0
        # while i < n:
        #     while i < n and s[i] == ' ':
        #         i += 1
        #     if i >= n: break
        #     j = i + 1
        #     while j < n and s[j] != ' ':
        #         j += 1
        #     stack.append(s[i:j])
        #     i = j + 1
        # stack = stack[::-1]
        # return " ".join(stack)