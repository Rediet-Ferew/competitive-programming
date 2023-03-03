# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        min_bad = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                min_bad = min(min_bad, mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_bad
