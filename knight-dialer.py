class Solution:
    def knightDialer(self, n: int) -> int:
        mod = (10 ** 9) + 7
        counts = {0: 2, 1: 2, 2: 2, 3: 2, 4: 3, 5: 0, 6: 3, 7: 2, 8: 2, 9: 2}
        pair = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 5: []}
        arr = []
        @cache
        def dp(i, num):
            if i == n - 1:
                # arr.append(cnt)
                return 1
            ct = 0
            for p in pair[num]:
                ct += dp(i + 1, p)
                # ct += counts[num]
            return ct
        c = 0
        for j in range(10):
            c += dp(0, j)
        # print(arr)
        return (c % mod)