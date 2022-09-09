class Solution:
    def minimumBuckets(self, street: str) -> int:
        val = 0
        n = len(street)
        streetList = [c for c in street]
        if street == 'H':
            return -1
        if street == '.':
            return 0
        if "HHH" in street:
            return -1
        for i in range(n):
            if streetList[i] == 'H':
                if i > 0 and streetList[i - 1] == 'B':
                    continue
                if i + 1 < n and streetList[i + 1] == '.':
                    streetList[i + 1] = 'B'
                    val += 1
               
                elif i > 0 and streetList[i - 1] == '.':
                    streetList[i - 1] = 'B'
                    val += 1
                    
                else:
                    return -1
                    
        print(streetList)
        return val
                
                
    
        # streetList = [c for c in street]
        # if n == 1 and street[0] == 'H':
        #     return -1
        # if n == 1 and street[0] == '.':
        #     return 0
        # if streetList[0] == 'H' and streetList[1] != '.':
        #     val = -1
        # elif streetList[0] == 'H' and streetList[1] == '.':
        #     streetList[1] = 'B'
        #     val += 1
        # if streetList[n - 1] == 'H' and streetList[n - 2] != '.':
        #     val = -1
        # elif streetList[n - 1] == 'H' and streetList[n - 2] == '.':
        #     streetList[n - 2] = 'B'
        #     val += 1
        # for i in range(1, len(streetList) - 1):
        #     if streetList[i] == 'H' and streetList[i + 1] != '.' and streetList[i - 1] != '.':
        #         val = -1
        #         break
        #     elif streetList[i] == 'H' and streetList[i + 1] == '.' and streetList[i - 1] == '.':
        #         streetList[i + 1] = 'B'
        #         val += 1
        # # print(streetList)
        # # print(val)
        # return val