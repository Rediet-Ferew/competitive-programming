class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        import statistics
        n = len(nums)
        median = 0
        arr = [0] * (len(nums))
        nums = sorted(nums)
        middle = statistics.median(nums)
        # if n%2 == 0:
        #     middle = (nums[(n//2)- 1] + nums[n//2])//2
        # else:
        #     middle = nums[(n//2)- 1]
        odd = 1
        even = 0
        for i in range(len(nums)):
            if nums[i] < middle:
                arr[odd] = nums[i]
                odd+=2
            else:
                arr[even] = nums[i]
                even+=2
        return arr