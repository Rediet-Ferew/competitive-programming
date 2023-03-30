class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        freq = []
        for key, val in count.items():
            freq.append((val, key))
        target = len(freq)- k
        def quickSort(start, end):
            if start == end:
                return freq[start:]
            pivot = freq[start][0]
            l = start + 1
            r = start + 1
            while  r <= end:
                if freq[r][0] < pivot:
                    freq[r],freq[l] = freq[l], freq[r]
                    l += 1
                r += 1
            freq[start],freq[l-1] = freq[l-1], freq[start]
            if l - 1 == target:
                return freq[l - 1:]
            elif target > l -1:
                return quickSort(l,end)
            else:
                return quickSort(start,l-2)

        ans = quickSort(0,len(freq)-1)
        final = []
        for i in ans:
            v, k = i
            final.append(k)
        return final
