class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_set = set(words)
        max_len = 0
        for i in range(len(words)):
            words_set.remove(words[i])
            
            for word in list(words_set):
                if not (set(words[i])).intersection(set(word)):
                    max_len = max(max_len, len(words[i]) * len(word))
            words_set.add(words[i])
        return max_len
                    
