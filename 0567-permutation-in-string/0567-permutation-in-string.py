class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) < len(s1):
            return False
        count_s1 = {}
        sub_count = {}
        for i in range(len(s1)):
            count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)
            sub_count[s2[i]] = 1 + sub_count.get(s2[i], 0)
        if count_s1 == sub_count:
            return True
        left = 0
        right = n
        while right < len(s2):
            sub_count[s2[left]] -= 1
            sub_count[s2[right]] = 1 + sub_count.get(s2[right], 0)
            if sub_count[s2[left]] == 0:
                sub_count.pop(s2[left])
            if count_s1 == sub_count:
                return True
            left += 1
            right += 1
        return False