class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        2
        2, 5,6 , 4, 3, 7, 11
        k = 10
        2,  3, 4, 5,6,7,11
                 l              
                 r
        10 - 4 = 6
        """
        nums.sort()
        l = 0
        r = len(nums) - 1
        operations = 0
        while l < r:
            pair = k - nums[l]
            if nums[r] > pair:
                while l < r and nums[r] > pair:
                    r -= 1
            elif nums[r] < pair:
                l += 1
            else:
                r -= 1
                l += 1
                operations += 1
        return operations