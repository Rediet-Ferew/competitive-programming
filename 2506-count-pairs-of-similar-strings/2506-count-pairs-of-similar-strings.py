class Solution:
    def similarPairs(self, words: List[str]) -> int:
        char_set = {}
        pairs = 0
        for word in words:
            word_set = list(set(word))
            word_set.sort()
            # print(word_set
            word_s ="".join(word_set)
            if word_s not in char_set:
                char_set[word_s] = 1
            else:
                pairs += char_set[word_s]
                char_set[word_s] += 1
        return pairs