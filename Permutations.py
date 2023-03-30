class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        visited = 0
        # print(1 << 0)
        def backtrack(arr):
            nonlocal visited
            if len(arr) == n:
                res.append(arr.copy())
                return 
            for i in range(len(nums)):
                if (visited >> i) & 1:
                    continue
                arr.append(nums[i])
                #set the ith bit
                visited |= (1 << i)
                
                backtrack(arr)
                arr.pop()
                #turn off the ith bit
                visited &= (~(1 << i))
                
                # visited.remove(i)
        backtrack([])
        return res
                
                
