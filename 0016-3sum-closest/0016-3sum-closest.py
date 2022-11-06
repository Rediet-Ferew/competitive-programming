class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float("inf")
        for i, num in enumerate(nums):
            l = i + 1
            r = n - 1
            while l < r:
                total = num + nums[l] + nums[r]
                dis = abs(target - total)
                if dis < abs(target - closest):
                    closest = total
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    return total 
                    
        return closest