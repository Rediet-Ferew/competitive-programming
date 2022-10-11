class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        mod = k % total
        if mod == 0:
            return 0
        for i in range(len(chalk)):
            if mod >= chalk[i]:
                mod -= chalk[i]
            else:
                return i