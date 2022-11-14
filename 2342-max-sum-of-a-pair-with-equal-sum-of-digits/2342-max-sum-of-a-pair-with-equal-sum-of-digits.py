class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        [18,43,36,13,7]
        [10,12,19,14]
        [10,12,14,19]
        [7,13,18,36,43]
        1:10
        3:12
        5:14
        10:19
        """
        def find_sum(n):
            total = 0
            while n != 0:
                mod = n%10
                total += mod
                n = n//10
            return total
        nums.sort()
        sum_num = {}
        max_sum = float('-inf')
        for n in nums:
            d_sum = find_sum(n)
            if d_sum not in sum_num:
                sum_num[d_sum] = n
            else:
                curr_sum = sum_num[d_sum] + n
                max_sum = max(max_sum, curr_sum)
                sum_num[d_sum] = n
        return max_sum if max_sum != float('-inf') else -1
                
                
                