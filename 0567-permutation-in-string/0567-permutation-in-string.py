class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        
        freq_1 = Counter(s1)
        freq_2 = {}
        k = len(s1)
        if k > n:
            return False
        
        for i in range(k):
            
            if s2[i] in freq_2:
                freq_2[s2[i]] += 1
            else:
                freq_2[s2[i]] = 1
                
        if freq_1 == freq_2:
            return True

        left = 0
        for right in range(k, n):
            
            ch_l = s2[left]
            
            freq_2[ch_l] -= 1
            
            if freq_2[ch_l] == 0:
                freq_2.pop(ch_l)
            
            
            ch = s2[right]
            
            if ch in freq_2:
                freq_2[ch] += 1
            else:
                freq_2[ch] = 1
            left += 1
            
            if freq_1 == freq_2:
                return True
            
        return False
        