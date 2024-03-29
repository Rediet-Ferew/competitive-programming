class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)
        mod = n % (2*k)
        n_2k = n - mod
        l = 0
        r = (2 * k) - 1
        while r < n_2k:
            m = l + k - 1
            s[l: m + 1] = reversed(s[l:m + 1])
            l = r + 1
            r += (2 * k)
        if mod <= k:
            s[n_2k:] = reversed(s[n_2k:])
        elif mod > k and mod < (2*k):
            ln = n_2k + k 
            s[n_2k:ln] = reversed(s[n_2k:ln])
        return "".join(s)
       
        
        