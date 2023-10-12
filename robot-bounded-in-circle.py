class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        x, y -> -y, x anticlockwise
        x, y -> y, -x clockwise
        if "L" -> N -> W, W -> S, S -> E, E -> N
        if "R" -> N -> E, E -> S, S -> W, W -> N
        """
        left = {"N": "W", "W": "S", "S": "E", "E": "N"}
        right = {"N": "E", "E" : "S", "S": "W", "W": "N"}
        coor = [0, 0, "N"]
        for ch in instructions:
            if ch == "G":
                coor[1] += 1
            elif ch == "L":
                temp = coor
                coor = [-1 * temp[1], temp[0], left[coor[2]]]
            elif ch == "R":
                temp = coor
                coor = [temp[1], -1 * temp[0] ,right[coor[2]]]
        if coor == [0, 0, "N"]:
            return True
        elif coor[2] != "N":
            return True
        return False