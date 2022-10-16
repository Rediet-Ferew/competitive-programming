class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        prefix = []
        for i, num in enumerate(arr):
            prefix.append((num, abs(num - x)))
            
        prefix = sorted(prefix, key=lambda kv:
                 (kv[1], kv[0]))
        # print(prefix)
        prefix = prefix[:k]
        ans = []
        for pre in prefix:
            ans.append(pre[0])
        ans.sort()
        return ans