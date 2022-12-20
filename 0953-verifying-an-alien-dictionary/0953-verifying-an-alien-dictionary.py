class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {}
        for i, c in enumerate(order):
            alien_dict[c] = i
        for i in range(len(words) - 1):
        
            left, n_l = words[i], len(words[i])
            right, n_r = words[i+1], len(words[i+1])
            if left in right:
                continue
            elif right in left:
                return False
            
            j = 0
            while j < n_l and j < n_r and left[j] == right[j]:
                j += 1
            if j < n_l and j < n_r and alien_dict[left[j]] > alien_dict[right[j]]:
                return False
            elif j >= n_l or j >= n_r:
                return False
        return True
                