class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        aaabbc -> aabbbc
        bbccca -> abbccc
        """
        w1 = sorted(word1)  #logn
        w2 = sorted(word2)  #logn
        if w1 == w2:
            return True
        w1_count = Counter(word1)
        w2_count = Counter(word2)
        freq1 = sorted(w1_count.values())
        freq2 = sorted(w2_count.values())
        if freq1 == freq2 and sorted(w2_count.keys()) == sorted(w1_count.keys()):
            return True
        return False
        