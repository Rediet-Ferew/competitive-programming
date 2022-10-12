class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        curr_score, max_score = 0, 0
        tokens.sort()
        while tokens:
            if power >= tokens[0]:
                token = tokens[0]
                del tokens[0]
                power -= token
                curr_score += 1
                max_score = max(max_score, curr_score)
            elif curr_score > 0:
                gain = tokens.pop()
                power += gain
                curr_score -= 1
            else:
                break
        return max_score