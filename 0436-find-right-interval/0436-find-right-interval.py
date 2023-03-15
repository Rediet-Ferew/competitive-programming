class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = {}
        
        for i in range(n):
            starts[intervals[i][0]] = i
            
        st = list(starts.keys())
        st.sort()
        res = []
        
        for j in range(n):
            
            r = bisect_right(st, intervals[j][1])
            
            if r > 0 and st[r - 1] == intervals[j][1]:
                res.append(starts[st[r - 1]])
                
            elif r >= n:
                res.append(-1)
                
            else:
                res.append(starts[st[r]])
                
        return res
                