class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left = 0
        right = (n - k)
        curr_score = sum(cardPoints[right:])
        score = curr_score
        while right <= n - 1:
            curr_score += cardPoints[left]
            curr_score -= cardPoints[right]
            score = max(curr_score, score)
            right += 1
            left += 1
        return score
        