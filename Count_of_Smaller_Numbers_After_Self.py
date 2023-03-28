class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        def mergeSort(left, right, nums):
            
            mid = (left + right)//2
            if left == right:
                return [[nums[left], left, 0]]
            
            left_list = mergeSort(left, mid, nums)
            right_list = mergeSort(mid + 1, right, nums)
            
            # print(left_list)
            # print(right_list)
            
            # ans = []
            for tpl in left_list:
                # print(tpl)
                r = bisect_right(right_list, tpl)
                # print(r)
                tpl[2] += r
                
                # ans.append((tpl[0], tpl[1] + r))
            merged = []
            lt = 0
            rt = 0
            while lt < len(left_list) and rt < len(right_list):
                if left_list[lt][0] < right_list[rt][0]:
                    merged.append(left_list[lt])
                    lt += 1
                    
                else:
                    merged.append(right_list[rt])
                    rt += 1
            while lt < len(left_list):
                merged.append(left_list[lt])
                lt += 1
            while rt < len(right_list):
                merged.append(right_list[rt])
                rt += 1
            
            return merged
        
        mrgd = mergeSort(0, len(nums) - 1, nums)
        # print(mrgd)
        final = [0] * len(nums)
        
        for j in range(len(mrgd)):
            
            num, idx, cnt = mrgd[j]
            final[idx] = cnt
            
        return final
    
        
        
        
