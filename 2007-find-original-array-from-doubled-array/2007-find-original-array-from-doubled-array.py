class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        changed.sort()
        original = []
        count = Counter(changed)
        for num in changed:
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                original.append(num)
            elif num != 0 and count[num] and count[num * 2]:
                count[num] -= 1
                count[num * 2] -= 1
                original.append(num)
        if len(original) == len(changed) // 2:
            return original
        else:
            return []