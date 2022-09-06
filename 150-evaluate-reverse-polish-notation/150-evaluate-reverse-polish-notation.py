class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = ['+', '/', '-', '*']
        for i in range(len(tokens)):
            x = tokens[i]
            if x in operation:
                first_num = int(stack.pop())
                second_num = int(stack.pop())
                result = 0
                if x == "+":
                    result = first_num + second_num
                elif x == "-":
                    result = second_num - first_num
                elif x == "*":
                    result = first_num * second_num
                else:
                    result = int(second_num / first_num)
                stack.append(str(result))
            else:
                stack.append(int(x))
                
        return int(stack[0])
                    