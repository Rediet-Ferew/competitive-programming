class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = (10**9) + 7
        powers = [2**i for i in range(0, 22)]
        power_pair = {}
        pairs = 0
        for d in deliciousness:
            for j in range(0,22):
                diff = powers[j] - d
                if diff in power_pair:
                    pairs += power_pair[diff]
            power_pair[d] = 1 + power_pair.get(d, 0)
        return (pairs%mod)