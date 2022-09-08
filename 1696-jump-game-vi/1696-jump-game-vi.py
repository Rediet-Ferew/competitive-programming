class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[n - 1] = nums[n - 1]
        heap = []
        heapq.heappush(heap, (-nums[n - 1], n - 1))
        for i in range(n - 2, -1, -1):
            while True:
                if i + k >= heap[0][1]:
                    dp[i] = nums[i] + heap[0][0] * -1
                    heapq.heappush(heap, (-dp[i], i))
                    break
                else:
                    heapq.heappop(heap)
        return dp[0]
        # dp = [0] * n
#         dp[0] = nums[0]
#         for i in range(1, n):
#             maxScore = 0
#             for j in range(1, k + 1):
#                 if i - j < 0: continue
                    
#                 maxScore = max(maxScore, dp[i - j])
#             dp[i] = maxScore + nums[i]
#         print(dp)