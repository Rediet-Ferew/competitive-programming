class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = []
        
        def backtrack(start,cnt, emps):
            
            if start >= len(requests):
                if all(v == 0 for v in emps):
                    res.append(cnt)
                else:
                    return
                return
           
            frm, to = requests[start]
            emps[frm] -= 1
            emps[to] += 1
            
            backtrack(start + 1, cnt + 1, emps)
            emps[frm] += 1
            emps[to] -= 1
            backtrack(start + 1, cnt, emps)
                
        emps = [0] * 20
      
        backtrack(0, 0, emps)
        return max(res)
        # return 0