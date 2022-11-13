class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
#         #odd index houses
#         odd_total = 0
#         for i in range(1, len(nums), 2):
#             odd_total += nums[i]
#         #even_index houses
#         even_total = 0
#         for j in range(0, len(nums), 2):
#             even_total += nums[j]
#         return odd_total if odd_total >= even_total else even_total
            
            