class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        result = []
        for i in range(len(arr) - 1, -1, -1):
            max_index = arr.index(max(arr[: i + 1]))
            if max_index != i:
                flip(max_index)
                flip(i)
                result.append(max_index + 1)
                result.append(i + 1)
        return result
                