class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = sum(arr)
        for i in range(len(arr) - 1):
            end = i + 1
            while end < len(arr):
                length = end - i + 1  
                if length % 2 != 0:
                    summ = sum(arr[i : end + 1])
                    res += summ
                end += 1
        return res