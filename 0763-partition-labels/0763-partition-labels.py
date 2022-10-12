class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}  # character mapped to its last occurence in the string
        for i, ch in enumerate(s):
            hashmap[ch] = i
        end ,size = 0, 0
        output = []
        for i, ch in enumerate(s):
            size += 1
            if hashmap[ch] > end:
                end = hashmap[ch]
            if i == end:
                output.append(size)
                size = 0
        return output