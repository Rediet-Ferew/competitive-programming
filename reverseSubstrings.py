class Solution:
    def reverseParentheses(self, s: str) -> str:
        words = []
        word = ""
        for x in s:
            if x != "(" and x != ")":
                word += x
            else:
                words.append(word)
                word = ""
        words = words[::-1]
        
        reverse = ''.join([str(item) for item in words])
        if len(words) == 2:
            return reverse[::-1]
        else:
            return reverse