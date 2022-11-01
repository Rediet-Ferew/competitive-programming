class Solution {
public:
    void sortColors(vector<int>& nums) {
        int l = 0;
        int r = 0;
        int end = nums.size() - 1;
        while(l <= end){
            if(nums[l] == 0){
                int temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
                l++;
                r++;
            }else if(nums[l] == 1){
                l++;
            }else{
                int temp = nums[l];
                nums[l] = nums[end];
                nums[end] = temp;
                end--;
            }
        }
        
    }
};