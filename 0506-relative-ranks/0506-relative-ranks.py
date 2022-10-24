class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        nums = sorted(score)
        n = len(nums)
        
        preMap = {}
        answer = [0] * n
        for idx, num in enumerate(score):
            preMap[num] = idx
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                idx = preMap[nums[i]]
                answer[idx] = "Gold Medal"
            elif i == n - 2:
                idx = preMap[nums[i]]
                answer[idx] = "Silver Medal"
            elif i == n - 3:
                idx = preMap[nums[i]]
                answer[idx] = "Bronze Medal"
            else:
                idx = preMap[nums[i]]
                answer[idx] = str(n - i)
        return answer
        