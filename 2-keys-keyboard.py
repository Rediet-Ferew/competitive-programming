class Solution:
    def minSteps(self, n: int) -> int:
        """
        copy, paste flag
        paste only copy is true
        else copy
        """
        memo = {}
        
        def dp(copy, s, copied):
            
            if (copy, s, copied) in memo:
                return memo[(copy, s, copied)]
            if len(s) > n:
                return 1000000
            if len(s) == n:
                
                return 0 
            
            op_1, op_2, op_3 = 100000, 100000, 100000
            if copy:
                op_1 = dp(copy, s + copied, copied) + 1
                op_2 = dp(not copy, s + copied, "") + 1
                
            else:
                op_3 = dp(not copy, s, s) + 1
            
            memo[(copy, s, copied)] = min(op_1, op_2, op_3)
            return memo[(copy, s, copied)]
        
        return dp(False, 'A', "")