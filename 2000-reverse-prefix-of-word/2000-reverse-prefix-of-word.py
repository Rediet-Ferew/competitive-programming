class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        idx = 0
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break
        # print(idx)
        start = 0
        end = idx
        while start < end:
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
        return ("".join(word))
            
        
        