class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        l = len(queries)
        ans = []
        
        for i, n in enumerate(nums):
            if n % 2 == 0:
                even_sum += n
                
        
        for j in range(l):
            val, idx = queries[j]
            res = nums[idx] + val
            
            if res % 2 == 0 and nums[idx] % 2 == 0:
                even_sum -= nums[idx]
                even_sum += res
                
            elif res % 2 == 0 and nums[idx] % 2 != 0:
                even_sum += res
                
            elif res % 2 != 0 and nums[idx] % 2 == 0:
                even_sum -= nums[idx]
                
            nums[idx] = res
            ans.append(even_sum)
            
        return ans