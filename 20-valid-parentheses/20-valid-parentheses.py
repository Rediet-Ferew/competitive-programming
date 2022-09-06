class Solution:
    def isValid(self, s: str) -> bool:
        list1 = []
        list2 = []
        list3 = []
        braces = {'(': ')', '[':']', '{':'}'}
        if len(s) == 0 or len(s) == 1 or s[0] in braces.values():
            return False
        for brace in s:
            if brace in braces.keys():
                list1.append(brace)
            elif brace in braces.values():
                list2.append(brace)
        if len(list1) != len(list2):
            return False
        for brace in s:
            if brace == '(' or brace =='{' or brace == '[':
                list3.append(brace)
            if brace == ')' or brace == ']' or brace == '}':
                if list3 and braces[list3[-1]] == brace:
                    list3.pop()
           
        if len(list3) != 0: 
            return False
        else:
            return True