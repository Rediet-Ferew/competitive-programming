class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
              
        max_deque = deque() # monotonically decreasing deque, stores indices
        min_deque = deque() # monotonically increasing deque, stores indices
        longest_subarray = window_start = 0

        for window_end in range(len(nums)):
            while max_deque and nums[max_deque[-1]] < nums[window_end]:
                max_deque.pop()
            max_deque.append(window_end)

            while min_deque and nums[min_deque[-1]] > nums[window_end]:
                min_deque.pop()
            min_deque.append(window_end)

            while abs(nums[max_deque[0]] - nums[min_deque[0]]) > limit:
                if min_deque and min_deque[0] == window_start:
                    min_deque.popleft()

                if max_deque and max_deque[0] == window_start:
                    max_deque.popleft()

                window_start += 1

            longest_subarray = max(longest_subarray, window_end - window_start + 1)
        return longest_subarray