class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        max_area = 0
        small_right = [n for i in range(n)]
        small_left = [n for i in range(n)]
        
        stack = []

        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                small_right[i] = stack[-1]
            stack.append(i)

        stack.clear()

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left = -1 if not stack else stack[-1]
            small_left[i] = left
            stack.append(i)

        for i in range(n):
            small_left[i] += 1
            small_right[i] -= 1
            cur_area = heights[i] * (small_right[i] - small_left[i] + 1)
            print(i, small_left[i], small_right[i], cur_area)
            max_area = max(max_area, cur_area)

        return max_area