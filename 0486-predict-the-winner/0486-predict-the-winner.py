class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        l = 0
        r = len(nums) - 1
        score1, score2 = 0, 0
        turn_1 = 1
        def searchPath(l, r, score1, score2, turn_1):
            
            if l > r:
                return score1 >= score2
            
            if turn_1:
                return searchPath(l + 1, r, score1 + nums[l], score2, turn_1 - 1) or searchPath(l, r - 1, score1 + nums[r], score2, turn_1 - 1)
            else:
                return searchPath(l + 1, r, score1, score2 + nums[l], turn_1 + 1) and searchPath(l, r - 1, score1, score2 + nums[r], turn_1 + 1)
            
        return searchPath(l, r, score1, score2, turn_1)