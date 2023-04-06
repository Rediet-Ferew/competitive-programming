class Solution:
    def countArrangement(self, n: int) -> int:
        visited = 0
        
        cnt = 0
        #find permutations
        #have to use pruning
        def backtrack(arr):
            nonlocal visited
            nonlocal cnt
            if len(arr) == n:
                
                cnt += 1
                return
            for i in range(1, n + 1):
                if (visited >> i) & 1:
                    continue
                if i % (len(arr) + 1) != 0 and (len(arr) + 1) % i != 0:
                    continue
                arr.append(i)
                visited |= (1 << i)
                # print(arr)
                backtrack(arr)
                arr.pop()
                visited &= (~(1 << i))
            return cnt
        return backtrack([])
