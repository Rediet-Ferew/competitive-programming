class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        k = (n*5)//100
        arr.sort()
        arr = arr[n//20: -n//20]
        
        total = sum(arr)
        mn = total / ((n * 9)//10)
       
        return mn 