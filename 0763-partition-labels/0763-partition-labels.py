class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        n = len(s)
        
        for idx, ch in enumerate(s):
            last_idx[ch] = idx
        
        part_idx = 0
        i = 0
        partitions = []
        count = 1
        while i < n:
            end = last_idx[s[i]]
            # print(end)
            if end > part_idx:
                part_idx = last_idx[s[i]] 
            
            if i == part_idx:
                partitions.append(count)
                count = 0
                
            count += 1
            i += 1
        return partitions