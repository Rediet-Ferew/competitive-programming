class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        visited = {}
        for idx, num in enumerate(numbers):
            
            diff = target - num
            
            if diff in visited:
                indx = visited[diff]
                
                return [indx + 1, idx + 1]
            
            visited[num] = idx
            
#         left = 0
#         right = n - 1
#         while left < right:
#             curr_sum = numbers[left] + numbers[right]
            
#             if curr_sum > target:
#                 right -= 1
#             elif curr_sum < target:
#                 left += 1
#             else:
#                 return [left + 1, right + 1]