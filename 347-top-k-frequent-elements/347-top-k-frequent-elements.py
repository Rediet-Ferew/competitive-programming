class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequent = []
        for val in count.values():
            frequent.append(val)
        frequent = sorted(frequent)
        final = []
        i = -1
        while k > 0:
            for key, freq in count.items():
                if freq == frequent[i]:
                    final.append(key)     
            k -= 1
            i -= 1
        return list(set(final))
       