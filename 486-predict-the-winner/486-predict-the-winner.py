class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp =[[0]*len(nums) for _ in range(len(nums))]
        for i in range(len(nums),-1,-1):
            for j in range(i,len(nums)):
                if i==j:dp[i][j] = nums[i]
                else:
                    left = nums[i] - dp[i+1][j]
                    right = nums[j] - dp[i][j - 1]
                    dp[i][j] = max(left,right)
        return dp[0][len(nums) -1] >= 0
            