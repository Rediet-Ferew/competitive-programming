class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = 1
        summation = 0
        set1 = set(arr)
        if len(set1) == 1:
            return 1
        from itertools import groupby
        count = [len(list(group)) for key, group in groupby(sorted(arr))]
        for i in range(len(count) - 1):
            summation += count[i] + count[i + 1]
            counter += 1
            if summation > len(arr)//2:
                break
        return counter
        