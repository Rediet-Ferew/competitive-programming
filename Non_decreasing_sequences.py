class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(nums, lst, pointer):
            nonlocal res

            if pointer >= len(nums):
                if lst not in res and len(lst) >= 2:
                    res.append(lst[:])

                return

            if not lst:
                helper(nums, lst + [nums[pointer]], pointer + 1)

            elif nums[pointer] >= lst[-1]:
                helper(nums, lst + [nums[pointer]], pointer + 1)

            helper(nums, lst, pointer + 1)

        helper(nums, [], 0)
        return res
