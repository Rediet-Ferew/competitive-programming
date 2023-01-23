class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        valids = []
        ans = []
        #8 directions 
        #left
        left = king[1] - 1
        while left >= 0:
            pair = [king[0], left]
            if pair in queens:
                ans.append(pair)
                break
            else:
                
                left -= 1
                continue
            
        #right
        right = king[1] + 1
        while right < 8:
            pair = [king[0], right]
            if pair in queens:
                ans.append(pair)
                break
            else: 
                right += 1
                continue
            
            
        
        #up
        up = king[0] - 1
        while up >= 0 :
            pair = [up, king[1]]
            if pair in queens:
                ans.append(pair)
                break
            else:
                
                up -= 1
                continue
        
        #down
        down = king[0] + 1
        while down < 8:
            
            pair = [down, king[1]]
            if pair in queens:
                ans.append(pair)
                break
            else:
                down += 1
                continue
        
        main_row = king[0] + 1
        main_col = king[1] + 1
        while main_row < 8 and main_col < 8:
            pair = [main_row, main_col]
            if pair in queens:
                ans.append(pair)
                break
            else:
                main_row += 1
                main_col += 1
                continue
            
        main_r = king[0] - 1
        main_c = king[1] - 1
        while main_r >= 0 and main_c >= 0:
            pair = [main_r, main_c]
            if pair in queens:
                ans.append(pair)
                break
            else:
                main_r -= 1
                main_c -= 1
                continue
                
        r = king[0] + 1
        c = king[1] - 1
        while r < 8 and c >= 0:
            pair = [r, c]
            if pair in queens:
                ans.append(pair)
                break
            r += 1
            c -= 1
            
        rw = king[0] - 1
        cl = king[1] + 1
        while rw >= 0 and cl < 8:
            pair = [rw, cl]
            if pair in queens:
                ans.append(pair)
                break
            else:
                rw -= 1
                cl += 1
                continue

        return ans