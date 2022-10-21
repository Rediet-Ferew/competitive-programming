class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_nums = Counter(nums)
        count = []
        for key, val in count_nums.items():
            heapq.heappush(count, (-val, key))
        result = []
        while k > 0:
            freq, num = heapq.heappop(count)
            result.append(num)
            k -= 1
        return result 
            
        