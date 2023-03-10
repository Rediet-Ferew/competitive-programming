class Solution:
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.reverse()
        def backtrack(start, arr):
            nonlocal min_fair
            if start == len(cookies):
                min_fair = min(min_fair, max(arr))
                # print(min_fair)
                return min_fair
            if max(arr) >= min_fair:
                return 
            for i in range(k):
                arr[i] += cookies[start]
                # print(arr)
                # print("***********")
                backtrack(start + 1, arr)
                arr[i] -= cookies[start]
                
        bucket = [0] * k
        min_fair = float('inf')
        backtrack(0, bucket)
        return min_fair
        
            
    