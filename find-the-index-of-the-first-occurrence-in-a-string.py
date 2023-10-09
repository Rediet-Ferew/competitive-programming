class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for i in range(len(haystack)):
        #     start = 0
        #     head = i
        #     cnt = 0
        #     while start < len(needle) and head < len(haystack):
        #         if haystack[head] == needle[start]:
        #             start += 1
        #             head += 1
        #             cnt += 1
        #         else:
        #             break
        #     if cnt == len(needle):
        #         return i
        # return -1
        a = 27
        pattern = 0
        m = len(needle)
        n = len(haystack)
        for idx, ch in enumerate(needle):
            asc = (ord(ch) - 97) + 1
            pattern += ((a ** (m - (idx + 1))) * asc)
         
        start = 0
        
        for idx, ch in enumerate(haystack[:m]):
            asc = (ord(ch) - 97) + 1
            start += ((a ** (m - (idx + 1))) * asc)
        
        if start == pattern:
            return 0
        left = 0
        right = m
        print(pattern)
        while right < n:
            
            asc = (ord(haystack[left]) - 97) + 1
            asc_r = (ord(haystack[right]) - 97) + 1
            p = start
            p -= ((a ** (m - 1)) * asc)
            p *= a
            p += ((a ** 0)*asc_r)
            start = p 
            if start == pattern:
                return left + 1
            print("*****")
            print(start)
            left += 1
            right += 1
        return -1