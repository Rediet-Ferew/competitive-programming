class Solution {
public:
    void reverseString(vector<char>& s) {
        // vector<char> word;
        // for(int i = 0; i < s.length; i++){
        //     word.pushback(s[i]);
        // }
        int l = 0;
        int r = s.size() - 1;
        while(l < r){
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            l++;
            r--;
        }
        
    }
};