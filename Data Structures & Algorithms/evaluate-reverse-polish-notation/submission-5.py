class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                
                if token == "+":
                    num1 = num1 + num2
                elif token == "-":
                    num1 = num1 - num2
                elif token == "*":
                    num1 = num1 * num2
                elif token == "/":
                    num1 = num1 / num2
                stack.append(int(num1))
        return stack[0]

