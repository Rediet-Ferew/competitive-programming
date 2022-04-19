

def sortSentence(self, s: str) -> str:
        
    sortedSentence = []
    word =  s.split()
    for i in range(len(word)):
        num = int(word[i][-1])
        word[num - 1], word[i] = word[i], word[num - 1]
    for j in word:
        sortedSentence.append(j[: -1])
    return ' '.join(map(str, sortedSentence))
               
