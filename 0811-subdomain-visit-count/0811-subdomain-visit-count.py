class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        n = len(cpdomains)
        domain_count = {}
        
        for i in range(n): #100
            domain = cpdomains[i]
            digit = 0
            
            #getting the digit for each domain
            j = 0
            while domain[j].isnumeric():  
                digit = digit * 10 + int(domain[j])
                j += 1
            
            #the domain after the number
            nxt_domain = domain[j+1:]
            domain_count[nxt_domain] = digit + domain_count.get(nxt_domain, 0)
            
            #separating each domain with dots and counting the number of times it occurs
            for idx in range(len(nxt_domain)):  
                
                if nxt_domain[idx] == '.':
                    nxt_nxt_domain = nxt_domain[idx+1:]
                    domain_count[nxt_nxt_domain] = digit + domain_count.get(nxt_nxt_domain, 0)
        
        #iterating through the dictionary to get all domain and count pairs
        res = []
        for k, v in domain_count.items(): #at most n times
            cp = ""
            cp += (str(v) + " " + k)
            res.append(cp)
        
        return res