class Solution {
    bool isVowel(char c){
            if(c == 'A' || c == 'a' || c == 'e' || c == 'E' || c == 'i' || c == 'I' || c == 'o' || c == 'O' || c == 'u' || c == 'U'){
                return true;
            }
            return false;
        }
public:
    string reverseVowels(string s) {
        int l = 0;
        int r = s.size() - 1;
        while(l < r){
            if(isVowel(s[l]) && isVowel(s[r])){
                char temp = s[l];
                s[l] = s[r];
                s[r] = temp;
                l++;
                r--;
            }else if(!isVowel(s[l])){
                l++;
            }else if(!isVowel(s[r])){
                r--;
            }
        }
        return s;
    }
};