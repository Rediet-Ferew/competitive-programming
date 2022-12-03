class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        count = Counter(s)
        list1 = sorted(count.items(), key=lambda kv:
                 (kv[1], kv[0]))
        empty = ""
        while list1:
            key, val = list1.pop()
            empty += (key * val)
        return empty