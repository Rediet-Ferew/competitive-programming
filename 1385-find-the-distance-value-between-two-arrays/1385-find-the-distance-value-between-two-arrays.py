class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        dis = 0
        
        for i in range(len(arr1)):
            flag = True
            for j in range(len(arr2)):
                ds = abs(arr1[i] - arr2[j])
                if ds <= d:
                    flag = False
                    break
            if flag:
                dis += 1
        return dis