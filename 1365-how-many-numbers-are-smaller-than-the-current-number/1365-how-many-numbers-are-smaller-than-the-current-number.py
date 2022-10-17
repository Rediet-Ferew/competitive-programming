class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        result = []
        for num in nums:
            if num in sortedNums:
                idx = sortedNums.index(num)
                result.append(idx)
                # sortedNums.pop()
        return result
        # counter = 0
        # mapping = {}
        # count = []
        # sortedNums = sorted(nums)
        # for i in range(len(sortedNums)):
        #     for num in sortedNums[: i]:
        #         if num < sortedNums[i]:
        #             counter += 1
        #     mapping[sortedNums[i]] = counter
        #     counter = 0
        # for val in nums:
        #     count.append(mapping[val])
        # return count
         
                