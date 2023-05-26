class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        sum_ = 0
        for i in range(len(nums)):
            #find average
            sum_ += nums[i]
            avg = math.ceil(sum_ / (i + 1))
            ans = max(ans, avg)
            
        return ans