class Solution:
    def minSwap(self, p: int, q: int):
        n = len(p)
        dp = [[-1, -1] for _ in range(n)]
        
        def rec(idx, prev):
            if idx == n:
                return 0
            
            if dp[idx][prev] != -1:
                return dp[idx][prev]
            
            ans = float('inf')
            
            prevP, prevQ = (0, 0)
            if idx != 0:
                if prev:
                    prevP = q[idx - 1]
                    prevQ = p[idx - 1]
                else:
                    prevP = p[idx - 1]
                    prevQ = q[idx - 1]
            
            if idx != 0:
                if (prevP >= p[idx] or prevQ >= q[idx]) and (prevQ >= p[idx] or prevP >= q[idx]):
                    return float('inf')
            
            if idx == 0:
                ans = min(ans, rec(idx + 1, False))  # No Swap
                ans = min(ans, 1 + rec(idx + 1, True))  # Swap
            else:
                if (prevP < p[idx] and prevQ < q[idx]) and (prevQ < p[idx] and prevP < q[idx]):
                    ans = min(ans, rec(idx + 1, False))  # No Swap
                    ans = min(ans, 1 + rec(idx + 1, True))  # Swap
                elif prevP >= p[idx] or prevQ >= q[idx]:
                    ans = min(ans, 1 + rec(idx + 1, True))  # Swap
                else:
                    ans = min(ans, rec(idx + 1, False))  # No need to swap
            
            dp[idx][prev] = ans
            return ans
        
        return rec(0, False)