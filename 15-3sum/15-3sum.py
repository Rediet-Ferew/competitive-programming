class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]: #avoiding duplicate calculation
                continue
                
            left = i + 1
            right = len(nums) - 1
            while left < right:
                summation = num + nums[left] + nums[right]
                if summation > 0:
                    right -= 1
                elif summation < 0:
                    left += 1
                else:
                    result.append([num, nums[left] ,nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result