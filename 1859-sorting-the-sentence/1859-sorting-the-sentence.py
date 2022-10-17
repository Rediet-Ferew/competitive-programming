class Solution:
    def sortSentence(self, s: str) -> str:
        
        senArr = s.split()
        sentence = [" "]*len(senArr)
        # words = {}
        # sentenceArray = s.split()
        # for word in sentenceArray:
        #     words[word[-1]] = word[:-1]
        # print(words)
        # for i in sorted(words):
        #     sentence.append(words[i]) 
        # return ' '.join(sentence)
        for word in senArr:
            # print(word[-1])
            idx = int(word[-1]) - 1
            sentence[idx] = word[:-1]
        return " ".join(sentence)