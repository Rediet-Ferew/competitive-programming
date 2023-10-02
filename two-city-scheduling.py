class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        A = []
        B = []

        for a, b in costs:
            if a <= b:
                A.append([abs(a - b), a, b])
            else:
                B.append([abs(a - b), a, b])
        if len(A) > len(B):
            A.sort(reverse = True)
            #sorteed by difference 
            while len(A) > len(B):
                B.append(A.pop())
        elif len(B) > len(A):
            B.sort(reverse = True)
            #sorteed by difference 
            while len(B) > len(A):
                A.append(B.pop())
        
        cost = 0
        for diff, a, b in A:
            cost += a
        for diff, a, b in B:
            cost += b
        return cost