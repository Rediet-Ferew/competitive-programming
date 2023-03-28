class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        total = []
        for j in range(len(nums1)):
            total.append(nums1[j] - nums2[j])
        # print(total)
        def mergeSort(left, right, arr, diff):
            nonlocal cnt
            mid = (left + right) // 2
            if left == right:
                return [arr[left]]
            left = mergeSort(left, mid, arr, diff)
            right = mergeSort(mid + 1, right, arr, diff)
            merged = []
            # print(left)
            # print(right)
            for i in range(len(right)):
                #get its index
                #get its first less element
                num = right[i] + diff
                l = bisect_right(left, num)
                print(l)
                
                cnt += (l)
                # if l < len(left) and left[l] == num:
                #     cnt += 1
                # cnt += i
            # cnt += len(right) - 1
            lt = 0
            rt = 0
            while lt < len(left) and rt < len(right):
                if left[lt] < right[rt]:
                    merged.append(left[lt])
                    lt += 1
                    
                else:
                    merged.append(right[rt])
                    rt += 1
            while lt < len(left):
                merged.append(left[lt])
                lt += 1
            while rt < len(right):
                merged.append(right[rt])
                rt += 1
            
            return merged
        
        cnt = 0
        mergeSort(0, len(total) - 1, total, diff)
        return cnt
        
