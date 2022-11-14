class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        # print(count)
        counts = [(val, key) for key, val in count.items()]
        counts = sorted(counts, key = lambda x:x[0])
        res = []
        another = {}
        for freq, n in counts:
            if freq not in another:
                another[freq] = [n]
            else:
                another[freq].append(n)
        for key, val in another.items():
            if len(val) == 1:
                for _ in range(key):
                    res.append(val[0])
            else:
                for n in sorted(val)[::-1]:
                    for _ in range(key):
                        res.append(n)
        return res