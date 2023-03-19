class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        num = 0
        div = [0] * n
        
        for d in range(n):
            # mod = int(word[i]) % m
            
            num = ((num * 10) + int(word[d])) % m
            if not num:
                div[d] = 1
                
        return div