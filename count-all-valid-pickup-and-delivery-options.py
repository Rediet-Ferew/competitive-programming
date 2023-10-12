class Solution:
    def countOrders(self, n: int) -> int:
        
        size = 2*n
        mod = 10**9 + 7
                
        return (math.factorial(size)//2**n) % mod