class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        times = n // 3
        output = []
        count = Counter(nums)
        print(count)
        for k, v in count.items():
            if count[k] > times:
                output.append(k)
        return output