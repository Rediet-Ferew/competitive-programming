class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        count = Counter(s)
        # print(count)
        # counte = {}
        
        # # list1 = list(counter.items())
        # # print(list1)
        # print(counter.items())
        list1 = sorted(count.items(), key=lambda kv:
                 (kv[1], kv[0]))
        print(list1)
        # for key, val in count.items():
        #     counte[val] = key
        # counte = OrderedDict(counte.items())
        # print(count.items())
        empty = ""
        while list1:
            key, val = list1[-1]
            list1.pop()
            empty += (key * val)
        return empty