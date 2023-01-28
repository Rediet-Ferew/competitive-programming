class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chem = 0
        l = 0
        r = len(skill) - 1
        total = skill[l] + skill[r]
        summation = 0
        while l < r:
            sum_ = skill[l] + skill[r]
            if sum_ == total:
                chem  += 1
                summation += (skill[l]*skill[r])
            l += 1
            r -= 1
        if chem == len(skill)//2:
            return summation
        return -1
            