class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        vals = count.values()
        return len(vals) == len(set(vals))