class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        def backtrack(start, curr_s, dots):
            
            if dots == 4 and start == len(s):
               
                result.append(curr_s[:-1])
                return 
            if dots > 4:
                return

            for i in range(start, min(start + 3,len(s))):
            
                if int(s[start:i+1]) <= 255 and (s[start] != "0" or start == i):
                    
                    backtrack(i + 1, curr_s + s[start:i+1] + ".", dots + 1)
           
        
        result = []
        backtrack(0, "" , 0)
        return result