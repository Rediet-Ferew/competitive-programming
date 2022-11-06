class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()
        for i in range(n):
            for j in range(i+1, n):
                l = j + 1
                r = n - 1
                while l < r:
                    total = nums[l]+ nums[r] + nums[i] + nums[j]
                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        temp = (nums[i], nums[j], nums[l], nums[r])
                        result.add(temp)
                        l += 1
                        r -= 1
                
        return list(result)