class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int l = 0;
        int r = 0;
        while(l < nums.size()){
            if(nums[l] != 0){
                int temp = nums[r];
                nums[r] = nums[l];
                nums[l] = temp;
                r++;
                l++;
            }
            else{
                l++;
            }
        }
    }
};