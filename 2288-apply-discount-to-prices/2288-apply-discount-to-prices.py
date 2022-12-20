class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(' ')
        for i in range(len(words)):
            if words[i][0] == '$':
                if words[i][1:].isnumeric():
                    temp = int(words[i][1:])
                    temp = temp - (temp * (discount/100))
                    
                    words[i] = f'${temp:.2f}'
            else:
                continue
        return " ".join(words)