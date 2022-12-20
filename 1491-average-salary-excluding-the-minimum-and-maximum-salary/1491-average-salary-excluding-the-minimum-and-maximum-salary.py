class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort() #logn
        n = len(salary)
        total = sum(salary[1:n-1]) #n
        return total/(n-2)