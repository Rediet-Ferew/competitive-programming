class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        without_comment = []
        line_ = ""
        block = False
        n = len(source)
        
        for i in range(n):
            m = len(source[i])
            line = source[i]
            j = 0
            while j < m:
                
                if not block:
                    
                    if j < m - 1 and line[j] == '/' and line[j + 1] == '/':
                        
                        break
                    elif j < m - 1 and line[j] == '/' and line[j + 1] == '*':
                        block = True
                        j = j + 2
                        
                    else:
                        line_ += line[j]
                        j += 1
                else:
                    if j < m - 1 and line[j] == '*' and line[j + 1] == '/':
                        block = False
                        j = j + 2
                    else:
                        j += 1
                        
            if not block and line_:
                without_comment.append(line_)
                line_ = ""
        return without_comment