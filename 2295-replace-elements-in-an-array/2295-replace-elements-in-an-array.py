class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        operations_map = {}
        m = len(operations)
        n = len(nums)
        
        
        for idx, num in enumerate(nums):
            operations_map[num] = idx
        
        for i in range(m):
            replaced, replacer = operations[i]
            
            idx = operations_map[replaced]
            nums[idx] = replacer
            operations_map.pop(replaced)
            operations_map[replacer] = idx
        
        return nums