class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        def test_kth(n, k):
            if (n & (1 << k)) != 0:
                return 1
            else:
                return 0
        for i in range(63):
            val1 = test_kth(x, i)
            val2 = test_kth(y, i)
            ans = val1 ^ val2
            
            if ans == 1:
                cnt += 1
            
        
        return cnt
