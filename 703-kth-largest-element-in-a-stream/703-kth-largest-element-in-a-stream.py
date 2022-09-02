class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # nums = [nums[i] for i in range(len(nums))]
        heapq.heapify(nums)
        self.numsHeap = nums
        print(self.numsHeap)
        while len(self.numsHeap) > k:
            heappop(self.numsHeap)
        

    def add(self, val: int) -> int:
        heappush(self.numsHeap, val)
        if len(self.numsHeap) > self.k:
            heappop(self.numsHeap)
        return self.numsHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)