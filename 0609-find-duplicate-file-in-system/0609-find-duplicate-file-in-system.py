class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = defaultdict(list)
        
        for directory in paths: #at most 20000000
            
            info = directory.split(' ')
            
            for file in info[1:]: #3000
                
                content = ""
                c = -2
                
                while file[c] != '(':
                    content += file[c]
                    c -= 1
                
                
                duplicates[content].append(info[0] + '/' + file[:c])
        
        res = []
        for key, val in duplicates.items():
            if len(val) > 1:
                res.append(val)
        return res
                    