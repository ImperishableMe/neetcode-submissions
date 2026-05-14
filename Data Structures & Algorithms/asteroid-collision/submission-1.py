class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Two directions:
        - ast going right, anything on the right (moving opps)
        """
        n = len(asteroids)
        keep = [True] * n
        stack = []

        for i, ast in enumerate(asteroids):
           # val = abs(ast)
           # print(ast, stack)
           if ast < 0:
                while stack and asteroids[stack[-1]] < abs(ast):
                    ind = stack.pop()
                    keep[ind] = False

                if not stack:
                    continue

                if asteroids[stack[-1]] == abs(ast):
                    ind = stack.pop()
                    keep[ind] = False
                    keep[i] = False
                else:
                    keep[i] = False 
           else:
                stack.append(i)

           # while stack and asteroids[stack[-1]] <= 
        return [
        val for i, val in enumerate(asteroids) if keep[i]
        ]
