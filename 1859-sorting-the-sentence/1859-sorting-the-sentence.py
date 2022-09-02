class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = []
        words = {}
        sentenceArray = s.split()
        for word in sentenceArray:
            words[word[-1]] = word[:-1]
        for i in sorted(words):
            sentence.append(words[i]) 
        return ' '.join(sentence)