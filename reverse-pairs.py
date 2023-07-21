class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt = 0

        def merge(left, right):
            nonlocal cnt
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= 2*right[j]:
                    i += 1
                else:
                    cnt += len(left)-i
                    j += 1

            return sorted(left+right)


        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            return merge(mergeSort(arr[:(len(arr) + 1) // 2]), mergeSort(arr[(len(arr) + 1) // 2:]))

        mergeSort(nums)
        return cnt