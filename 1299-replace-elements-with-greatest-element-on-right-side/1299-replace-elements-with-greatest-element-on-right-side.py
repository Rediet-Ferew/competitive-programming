class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = arr[-1]
        arr[-1] = -1
        n = len(arr)
        for i in range(n-2, -1, -1):
            temp = arr[i]
            arr[i] = curr_max
            if temp > curr_max:
                curr_max = temp
        return arr