class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        all_combinations = []
        check = []
        counter = 1
        summation = sum(nums)
        for x in nums:
            if x == k:
                return 1
        if summation == k:
            return n
        else:
            for i in range(len(nums)):
                combinations_object = itertools.combinations(nums, i)
                combinations_list = list(combinations_object)
                all_combinations += combinations_list
            for sums in all_combinations:
                if sum(sums) < k:
                    n = -1
                elif sum(sums) == k:
                    n = len(sums)
                    break
                elif sum(sums) > k:
                    n = len(sums)
                    break
            return n
            
                
        
                       
            
            