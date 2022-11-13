class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1: #base case permutaion of length one is one
            return [nums.copy()] #copy the num so it can't be changed later
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
    