class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        left, right, counter = 0, k, 0
        target = threshold * k
        total = sum(arr[0 : k])
        if total >= target:
            counter += 1
        while right < n:
            total -= arr[left]
            total += arr[right]
            if total >= target:
                counter += 1    
            left += 1
            right += 1
        return counter
        