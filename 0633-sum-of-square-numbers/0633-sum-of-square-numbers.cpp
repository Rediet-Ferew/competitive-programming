class Solution {
public:
    bool judgeSquareSum(int c) {
        long l = 0;
        long r = floor(pow(c, 0.5));
        while (l <= r){
            long total = pow(l, 2) + pow(r, 2);
            if (total == c){
                return true;
            }else if(total < c){
                l++;
            }else{
                r--;
            }
        }
        return false;
    }
};