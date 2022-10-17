class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = []
        arr = s.split()
        for ch in arr:
            if ch.isnumeric():
                nums.append(int(ch))
        # print(arr)
        # print(nums)
        sortedSet = set(sorted(nums))
        sortedNum = sorted(nums)
        return (nums == sortedNum) and len(nums) == len(sortedSet)