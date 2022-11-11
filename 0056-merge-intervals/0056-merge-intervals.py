class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [[1,4],[4,5]]
        [[1,5]]
        
        """
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            end_prev = res[-1][1]
            end_now = intervals[i][1]
            if intervals[i][0] <= end_prev:
                res[-1][1] = max(end_prev, end_now)
            else:
                res.append(intervals[i])
        return res
        