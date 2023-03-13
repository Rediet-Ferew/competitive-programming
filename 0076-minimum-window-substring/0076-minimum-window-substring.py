class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        curr = 0
        n_map = {}
        h_map = {}

        res = float('inf')
        res_list = [0,len(s)]

        for i in t:
            n_map[i] = 1 + n_map.get(i,0)

        num = len(n_map)    

        l = 0 

        for r in range(len(s)):

            h_map[s[r]] = 1 + h_map.get(s[r],0)

            if s[r] in n_map and h_map[s[r]]==n_map[s[r]]:
                curr+=1

            while curr==num:
    
                if (r-l+1)<res:
                    res = r-l+1
                    res_list = [l,r]

                h_map[s[l]]-=1   

                if s[l] in n_map and h_map[s[l]]<n_map[s[l]]:
                    curr-=1

                l+=1               

        l,r = res_list

        return s[l:r+1] if res!=float('inf') else ""
        
        
        