class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        counter = 1
        if len(chars) == 1:
            s += chars[0]
        else:
            for i in range(len(chars) - 1):
                if chars[i] == chars[i + 1]:
                    counter += 1
                else:
                    if counter == 1:
                        s += chars[i]
                    else:
                        s += chars[i] + str(counter)
                        counter = 1
            
            if (counter == 1 ):
                s += chars[len(chars) - 1]
            else:
                s += chars[len(chars) - 1] + str(counter)
            
        chars.clear()
        for c in s:
            chars.append(c)
     
            
            