class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        new = []
        checker = True
        for i, j in zip(l, r):
            new = nums[i : j + 1]
            
            new = sorted(new)
            
            diff = new[1] - new[0]
            for k in range(len(new) - 1):
                if new[k + 1] - new[k] == diff:
                    checker = True
                else:
                    checker = False
                    break
            answer.append(checker)
        return answer