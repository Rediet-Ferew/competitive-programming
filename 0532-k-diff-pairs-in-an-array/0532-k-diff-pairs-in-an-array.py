class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        unique = set()
        hashset = {}
        num_set = sorted(nums)
        for i, n in enumerate(nums):
            hashset[n] = (k+n, -k+(n))
        for idx,num in enumerate(num_set):
            if hashset[num][0] in num_set[idx+1:]:
                unique.add((num,hashset[num][0]))
            if hashset[num][1] in num_set[idx+1:]:
                unique.add((num,hashset[num][1]))
        return len(unique)