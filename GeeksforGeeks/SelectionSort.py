class Solution: 
    def select(self, arr, i):
        m = len(arr)
        min_idx = i
        
        for idx in range(i + 1, m):
            if arr[idx] < arr[min_idx]:
                min_idx = idx
        return min_idx
    def selectionSort(self, arr,n):
        for j in range(n - 1):
            min_i = self.select(arr, j + 1)
            arr[j], arr[min_i] = arr[min_i], arr[j]
        return arr
