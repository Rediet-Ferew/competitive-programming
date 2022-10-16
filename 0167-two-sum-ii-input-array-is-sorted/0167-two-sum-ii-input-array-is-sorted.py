class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #prefix sum solution
        # prefix = {}
#         for i, num in enumerate(numbers):
#             diff = target - num
#             if diff in prefix:
#                 return [prefix[diff] + 1, i + 1]
#             prefix[num] = i
        # return

        n = len(numbers)
        left = 0
        right = n - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return 
