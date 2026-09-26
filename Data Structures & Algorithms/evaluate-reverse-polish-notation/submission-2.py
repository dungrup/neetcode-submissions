class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            if token == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 + val2)
            elif token == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif token == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(float(val2) / val1))
            elif token == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 * val1)
            else:
                stack.append(int(token))

        return int(stack[-1])