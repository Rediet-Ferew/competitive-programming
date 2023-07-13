class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        memo = {}
        ans = 0

        for i in range(n):
            diff = arr[i] - difference
            if diff not in memo:
                memo[arr[i]] = 1
            else:
                memo[arr[i]] = memo[diff] + 1
            ans = max(ans, memo[arr[i]])
        return ans
