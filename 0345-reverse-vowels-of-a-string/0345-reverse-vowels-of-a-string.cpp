class Solution {
    bool isVowel(char c){
            if(c == 'A' || c == 'a' || c == 'e' || c == 'E' || c == 'i' || c == 'I' || c == 'o' || c == 'O' || c == 'u' || c == 'U'){
                return true;
            }
            return false;
        }
public:
    string reverseVowels(string s) {
        vector<char> word;
        for(int i =0; i<s.size(); i++){
            word.push_back(s[i]);
        }
        
        int l = 0;
        int r = s.size() - 1;
        while(l < r){
            if(isVowel(word[l]) && isVowel(word[r])){
                char temp = word[l];
                word[l] = word[r];
                word[r] = temp;
                l++;
                r--;
            }else if(!isVowel(word[l])){
                l++;
            }else if(!isVowel(word[r])){
                r--;
            }
        }
        string res;
        for(int i = 0; i < word.size(); i++){
            res.push_back(word[i]);
        }
        return res;
    }
};