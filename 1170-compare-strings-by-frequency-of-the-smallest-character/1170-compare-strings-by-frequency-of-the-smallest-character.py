class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        n = len(words)
        def findFreq(s):
            s_l = list(s)
            s_l.sort()
            small = s_l[0]
            cnt = 0
            for i in range(len(s)):
                if s_l[i] == small:
                    cnt += 1
                else:
                    break
            return cnt
        arr = []
        for word in words:
            cnt = findFreq(word)
            arr.append(cnt)
        arr.sort()
        ans = []
        for q in queries:
            
            freq = findFreq(q)
            start = bisect_right(arr, freq)
            
            if start > n - 1:
                ans.append(0)
            else:
                nums = n - (start)
                ans.append(nums)
        
        return ans
            