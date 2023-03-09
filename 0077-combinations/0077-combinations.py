class Solution:
    def backtrack(self,n, l, curr, k, res):
        if len(l) == k:
            res.append(l.copy())
            return
        for c in range(curr, n + 1):
            l.append(c)
            # print(l)
            # print("*********")
            self.backtrack(n, l, c + 1,k, res) #done with the process then pop
            l.pop() 
            # print(l)
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtrack(n, [], 1 , k, result)
        return result
        
        