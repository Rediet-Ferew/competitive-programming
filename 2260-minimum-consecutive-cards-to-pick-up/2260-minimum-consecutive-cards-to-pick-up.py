class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        prefix = {}
        min_len = (10 ** 5) + 1
        for i, card in enumerate(cards):
            if card not in prefix:
                prefix[card] = i
            else:
                idx = prefix[card]
                length = (i - idx) + 1
                min_len = min(length, min_len)
                prefix[card] = i
            
        if min_len == (10 ** 5) + 1:
            return -1
        else:
            return min_len