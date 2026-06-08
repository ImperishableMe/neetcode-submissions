import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ind = bisect.bisect_right(matrix, target, key=lambda p: p[0])
        ind2 = bisect.bisect_right(matrix[ind-1], target)
        return ind2 > 0 and matrix[ind - 1][ind2 - 1] == target