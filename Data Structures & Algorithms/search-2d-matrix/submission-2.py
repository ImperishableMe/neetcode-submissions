import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = bisect.bisect_right(matrix, target, key=lambda p: p[0])
        # assert row != 0
        if row == 0:
            return False
        row -= 1
        col = bisect.bisect_right(matrix[row], target)
        return col > 0 and matrix[row][col - 1] == target