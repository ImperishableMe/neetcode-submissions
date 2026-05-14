class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack: list[str] = [] # stores unmatched open brackets

        for c in s:
            if c in brackets:
                # c is open bracket
                stack.append(c)
            else:
                if len(stack) > 0 and brackets[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return not len(stack) > 0