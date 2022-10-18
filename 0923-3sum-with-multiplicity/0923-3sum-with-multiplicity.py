import itertools
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = (10**9) + 7
        result = 0
        count = Counter(arr)
        nums = sorted(count)
        for i, num1 in enumerate(nums):
            j = i
            k = len(nums) - 1
            temp = target - num1
            while j <= k:
                num2, num3 = nums[j], nums[k]
                if num2 + num3 < temp:
                    j += 1
                elif num2 + num3 > temp:
                    k -= 1
                else:
                    if (i < j < k):
                        result += count[num1] * count[num2] * count[num3]
                    elif (i == j < k):
                        result += count[num1] * (count[num2] - 1) / 2 * count[num3]
                    elif (i < j == k):
                        result += count[num1] * count[num2] * (count[num3] - 1) / 2
                    else:
                        result += count[num1] * (count[num2] - 1) * (count[num3] - 2) / 6
                        
                    j += 1
                    k -= 1
        return int(result % mod)
        # count_Arr = [0] * 101
        # for num in arr:
        #     count_Arr[num] += 1
        # for i in range(101):
        #     for j in range(i , 101):
        #         k = target - i - j 
        #         if k < 0 or k > 100:
        #             continue
        #         if (i == j == k):
        #             result += (count_Arr[i] * (count_Arr[i] - 1) * (count_Arr[i] - 2)) / 6
        #         elif (i == j and j < k):
        #             result += (((count_Arr[i] * (count_Arr[i] - 1)) / 2) * count_Arr[k])
        #         elif (i < j and j < k):
        #             result += (count_Arr[i] * count_Arr[j] * count_Arr[k])
        # # result = result % mod
        # print(int(result % mod))