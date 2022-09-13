class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = []
        for n in num:
            while k > 0 and nums and nums[-1] > n:
                k -= 1
                nums.pop()
            nums.append(n)
        nums = nums[: len(nums) - k]
        result = "".join(nums)
        if result:
            return str(int(result))
        
        else:
            return "0"
                
        