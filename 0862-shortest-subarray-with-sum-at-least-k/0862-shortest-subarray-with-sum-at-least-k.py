class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])
            # prefix[i] += prefix[i - 1]
            
#         prefix = prefix[1:]
        
        # print(prefix)
        q = collections.deque([])
        min_len = float('inf')
        for idx, p in enumerate(prefix):
            # print(idx, p)
            if not q:
                q.append(idx)
                
            else:
                while q and p < prefix[q[-1]]:
                    # print(q[-1])
                    # print(q[-1][0])
                    q.pop()
                while q and prefix[q[0]] <= p - k:
                    min_len  = min(min_len, idx - q[0])
                    # print(q[0][0])
                    q.popleft() 
                    
                q.append(idx)
            
            # print(q)
        if min_len == float('inf'):
            return -1
        else:
            return min_len