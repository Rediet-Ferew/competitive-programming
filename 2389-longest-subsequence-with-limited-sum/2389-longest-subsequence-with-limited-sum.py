class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        [4,5,2,1]
        [1,2,4,5]
        7
        """
        n = len(nums)
        res = []
        nums.sort()
        suffix = sum(nums)
        for query in queries:
            total = suffix
            if query >= total:
                res.append(n)
            elif query < nums[0]:
                res.append(0)
            else:
                r = n - 1
                while r >= 0:
                    if total > query:
                        total -= nums[r]
                        r-=1
                    else:
                        res.append(r+1)
                        break
        return res