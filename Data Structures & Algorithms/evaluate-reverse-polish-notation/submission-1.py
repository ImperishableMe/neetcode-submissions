class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # holds the operands
        fns = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }

        for token in tokens:
            if token in fns:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(fns[token](val1, val2))
            else:
                stack.append(int(token))
        
        assert len(stack) == 1
        return stack[-1]
