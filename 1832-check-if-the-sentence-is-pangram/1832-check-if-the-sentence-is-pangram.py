class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        alphas = list(alphas)
        for i in range(26):
            if alphas[-1] in sentence:
                alphas.pop()
        return not (alphas)
        # charSet = set()
        # for letter in sentence:
        #     charSet.add(letter)
        # return len(charSet) == len(sentence)