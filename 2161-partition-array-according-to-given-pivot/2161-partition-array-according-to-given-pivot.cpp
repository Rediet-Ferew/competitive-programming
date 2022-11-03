class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> result(nums.size(), 0);
        int l = 0;
        int n = nums.size();
        int r = n - 1;
        for(int i = 0; i < n; i++){
            if(nums[i] < pivot){
                result[l] = nums[i];
                l++;
            }
            if(nums[n - i - 1] > pivot){
                result[r] = nums[n - i - 1];
                r--;
            }
        }
        while(l <= r){
            result[l] = pivot;
            l++;
        }
        return result;
    }
};