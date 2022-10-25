class Solution {
public:
    string reverseOnlyLetters(string s) {
        int n = s.length();
        int left = 0;
        int right = n - 1;
        char s_arr[n + 1];
        strcpy(s_arr, s.c_str());
        while (left < right){
            if (!isalpha(s_arr[left])){
                left++;
            } else if (!isalpha(s_arr[right])){
                right--;
            } else if ((isalpha(s_arr[left])) && (isalpha(s_arr[right]))){
                char temp = s_arr[left];
                s_arr[left] = s_arr[right];
                s_arr[right] = temp;
                left++;
                right--;
            }
        }
        int i;
        string res = "";
        for (i = 0; i < n; i++) {
            res = res + s_arr[i];
        }
        return res;
    }
};