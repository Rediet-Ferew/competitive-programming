class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_A = (ax2  - ax1) * (ay2  - ay1)
        area_B = (bx2  - bx1) * (by2 - by1)
        abx1 = max(ax1, bx1)
        abx2 = min(ax2, bx2)
        aby1 = max(ay1, by1)
        aby2 = min(ay2, by2)
        area_AB = (max(abx2  - abx1, 0)) * (max(aby2  - aby1, 0))
        total_area = (area_A + area_B) - area_AB
        return total_area