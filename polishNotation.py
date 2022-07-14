
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        results = []
        for x in tokens:
            if x != "+" and x != "/" and x != "-" and x != "*" :
                results.append(int(x))
            else:
                if x == "+":
                    result = int(results.pop()) + int(results.pop())
                elif x == "-":
                    first_num = int(results.pop())
                    second_num = int(results.pop())
                    result = second_num - first_num
                   
                elif x == "*":
                    first_num = int(results.pop())
                    second_num = int(results.pop())
                    result = first_num * second_num
                    
                elif x == "/":
                    first_num = int(results.pop())
                    second_num = int(results.pop())
                    result = second_num // first_num
                results.append(result)
        return results[0]
                    