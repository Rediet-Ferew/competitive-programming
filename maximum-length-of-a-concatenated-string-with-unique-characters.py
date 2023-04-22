class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = []
        
        def is_unique(s):
            visited = set()
            for i in range(len(s)):
                if s[i] not in visited:
                    visited.add(s[i])
                else:
                    return False
            return True
        def backtrack(start, bucket):
            # nonlocal max_len
            st = "".join(bucket)
            # # print(st)
            if not is_unique(st):
                return
            if start == len(arr):
                st = "".join(bucket)
                
                return
            

            s = arr[start]
            
            bucket.append(s)
            
            # print(bucket)
            res.append("".join(bucket.copy()))
            backtrack(start + 1, bucket)
            bucket.pop()
            backtrack(start + 1, bucket)
                    
        backtrack(0, [])
        
        max_len = 0
        for word in res:
            if is_unique(word):
                max_len = max(max_len, len(word))
        return max_len