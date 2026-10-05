class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if stack and i in ['-', '+', '*', '/']:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '-':
                    stack.append(a - b)
                elif i == '+':
                    stack.append(a + b)
                elif i == '*':
                    stack.append(a * b)
                else:
                    stack.append(a / b)
            else:
                stack.append(i)
        return int(stack[0])


        