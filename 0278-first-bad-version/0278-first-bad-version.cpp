// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long long int start = 1;
        long long int end = n ;
        long long int badVersion = 0;
        while (start <= end){
            long long int mid = floor((start + end) /2);
            if (!isBadVersion(mid)){
                start = mid + 1;
            }else{
                badVersion = mid;
                end = mid - 1;
            }
            
        }
        return badVersion;
    }
};