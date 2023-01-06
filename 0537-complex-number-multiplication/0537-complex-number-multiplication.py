class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        c_num1 = num1.split("+")
        c_num2 = num2.split("+")
        real1 = int(c_num1[0])
        real2 = int(c_num2[0])
        im1 = int(c_num1[1][:-1])
        im2 = int(c_num2[1][:-1])
        
        ans_real = (real1*real2) - (im1*im2)
        ans_im = (real1 * im2) + (im1 * real2)
        ans = str(ans_real) + "+" + (str(ans_im) + "i")
        
        return ans
        