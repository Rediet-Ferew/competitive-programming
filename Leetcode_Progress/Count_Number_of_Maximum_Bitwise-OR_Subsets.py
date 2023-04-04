class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        # print(max_or)
        
        def backtrack(start, arr, res):
            if start >= len(nums):
                return 
            
            # if or_val == max_or:
            #     return 
            for i in range(start, len(nums)):
                arr.append(nums[i])
                # print(arr)
                res.append(arr.copy())
                backtrack(i + 1, arr, res)
                arr.pop()
        bucket = []
        backtrack(0, [], bucket)
        cnt = 0
        for ar in bucket:
            or_val = 0
            for j in range(len(ar)):
                or_val |= ar[j]
            if or_val == max_or:
                cnt += 1
        return cnt
