class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = [
            (num, i)
            for i, num in enumerate(nums)
        ]
        A.sort()
        l, r = 0, len(A) - 1
        while l < r:
            total = A[l][0] + A[r][0]
            # xxxxxxxxxxprint(total)
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return sorted([A[l][1], A[r][1]])
        return []