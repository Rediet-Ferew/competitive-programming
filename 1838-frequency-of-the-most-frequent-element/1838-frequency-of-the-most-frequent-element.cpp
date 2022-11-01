class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long l = 0;
        long r = 0;
        long total = 0;
        long res = 0;
        while(r < nums.size()){
            total = total +  nums[r];
            while(nums[r] * (r - l + 1) > total + k){
                total = total - nums[l];
                l++;
            }
            res = max(res, r - l + 1);
            r++;
        }
        return res;
    }
};