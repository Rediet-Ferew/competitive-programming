class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        # print(count)
        counter = 0
        if len(nums) == 1:
            return 0
        for num in nums:
            if k == 2 * num and len(nums) > 1:
                counter += (count[num]//2)
                count[num] = 0
                # count[k - num] = 0
            elif count[num] and count[k - num] and len(nums) > 1:
                counter += min(count[num], count[k - num])
                count[num] = 0
                count[k - num] = 0
            
        return counter
                
        