class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        bool check = std::find(std::begin(nums), std::end(nums), target) != std::end(nums);
        if(!check){
            nums.push_back(target);
            sort(nums.begin(), nums.end());
        }
        
        int l = 0;
        int r = nums.size() - 1;
        while(l <= r){
            int mid = floor((l + r) / 2);
            if(nums[mid] > target){
                r = mid - 1;
            }else if(nums[mid] < target){
                l = mid + 1;
            }else{
                return mid;
            }
        }
       
        return -1;
        
    }
};