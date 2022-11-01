class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> res(n,0);
        for (int i = 0; i < nums.size(); i++){
            int idx = (i + k) % n;
            res[idx] = nums[i];
        }
        for(int j = 0; j < res.size(); j++){
            nums[j] = res[j];
        }
    }
};