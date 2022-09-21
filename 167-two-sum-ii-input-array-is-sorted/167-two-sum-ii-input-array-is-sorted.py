class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prefix = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in prefix:
                return [prefix[diff] + 1, i + 1]
            prefix[num] = i
        return
       
                    
