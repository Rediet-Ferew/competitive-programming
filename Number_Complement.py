class Solution:
    def findComplement(self, num: int) -> int:
        #get the binary representation
        
        b_rep = bin(num)
        sign = b_rep[0]
        b_rep = b_rep[2:]
        b_rep = list(b_rep)
        for i in range(len(b_rep)):
            if b_rep[i] == '0':
                b_rep[i] = '1'
            else:
                b_rep[i] = '0'
        final = sign + 'b' + "".join(b_rep)
        
        return int(final, 2)
