class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = []
        for key, val in counter.items():
            if val > 1:
                result.append(key)
        for num in range(1, len(nums) + 1):
            if num not in counter:
                result.append(num)
            
        return result
       