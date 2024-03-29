class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1_count = Counter(word1)
        w2_count = Counter(word2)
        freq1 = sorted(w1_count.values())
        freq2 = sorted(w2_count.values())
        if freq1 == freq2 and sorted(w2_count.keys()) == sorted(w1_count.keys()):
            return True
        return False
        