class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        Map = {}
        answer = 0
        total = 0
        for idx, num in enumerate(hours):
            if num > 8:
                total += 1
            else:
                total -= 1
            if total not in Map:
                Map[total] = idx
            if total > 0:
                answer = idx + 1
            elif (total - 1) in Map:
                answer = max(answer, idx - Map[total - 1])
        return answer