class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for i in num:
            n = n * 10 + i
    
        sum_ = n + k
        ans = []
        
        while sum_ > 0:
            mod = sum_ % 10
            ans.append(mod)
            sum_ = sum_ // 10
            
        return ans[::-1]
    
        