class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return len(arr)
        temp = 0
        l = 0
        max_len = 0
        for r in range(1, len(arr)):
            if arr[r - 1] < arr[r]:
                if temp == -1:
                    max_len = max(max_len, r - l)
                    l = r - 1
                temp = -1
            elif arr[r - 1] > arr[r]:
                if temp == 1:
                    max_len = max(max_len, r - l)
                    l = r - 1
                temp = 1
            else:
                max_len = max(max_len, r - l)
                l = r
                temp = 0
        return max(max_len, r - l + 1)