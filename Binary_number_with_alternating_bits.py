class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def test_kth(n, k):
            if (n & (1 << k)) != 0:
                return 1
            else:
                return 0
        string_bn = bin(n)
        # print(string_bn)
        for i in range(1, len(string_bn) - 1):
            val1 = test_kth(n, i)
            val2 = test_kth(n, i - 1)
            if not (val1 ^ val2):
                return False
        return True
