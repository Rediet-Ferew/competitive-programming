
class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        largeIndex = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left <= n and arr[left] > arr[i]:
            largeIndex = left
        else:
            largeIndex = i
        if right <= right and arr[i] > arr[right]:
            largeIndex = right
        if largeIndex != i:
            arr[largeIndex], arr[i] = arr[i], arr[largeIndex]
            heapify(self, arr, n, largestIndex)
    def buildHeap(self,arr,n):
        for i in range((n//2) - 1, 0, -1):
            heapify(self, arr, n, i)
    def HeapSort(self, arr, n):
        buildHeap(arr, n)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            n = n -1
            heapify(self,arr, n, i)
        return arr
    