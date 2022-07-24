class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        slist = []
        slist[:0]=s
        nums = []
        
        operations = []
        for c in slist:
            if c == '/' or c == '*' or c == '+' or c == '-':
                operations.append(c)
            
            else:
                nums.append(c)
            
        while len(operations) > 0:
            if operations[-1] == '/':
                first = nums.pop()
                second = nums.pop()
                result =int(second) // int(first)
                nums.append(str(result))
            elif operations[-1] == '*':
                first = nums.pop()
                second = nums.pop()
                result = int(second) * int(first)
                nums.append(str(result))
            elif operations[-1] == '-':
                first = nums.pop()
                second = nums.pop()
                result = int(second) - int(first)
                nums.append(str(result))
            elif operations[-1] == '+':
                first = nums.pop()
                second = nums.pop()
                result = int(second) + int(first)
                nums.append(str(result))
            
            operations.pop()
        
        return int("".join(nums))
        